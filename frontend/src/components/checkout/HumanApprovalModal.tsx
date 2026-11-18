import React, { useState } from 'react';
import { AlertTriangle, ShieldCheck, X, Check, Lock, ExternalLink, Loader2 } from 'lucide-react';
import { api } from '../../services/api';

interface HumanApprovalModalProps {
  isOpen: boolean;
  onClose: () => void;
  product: {
    id: string;
    name: string;
    brand?: string;
    price: number;
    seller?: string;
    image_url?: string;
    url?: string;
  };
  onSuccess?: (externalUrl?: string) => void;
}

export const HumanApprovalModal: React.FC<HumanApprovalModalProps> = ({
  isOpen,
  onClose,
  product,
  onSuccess
}) => {
  const [loadingReview, setLoadingReview] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [reviewManifest, setReviewManifest] = useState<any>(null);
  const [resultState, setResultState] = useState<{ status: string; message: string; url?: string } | null>(null);

  React.useEffect(() => {
    if (isOpen && product?.id) {
      setResultState(null);
      setLoadingReview(true);
      api.reviewCheckout(product.id)
        .then((data) => setReviewManifest(data))
        .catch((err) => {
          // Fallback if review endpoint encounters network issue
          setReviewManifest({
            product_id: product.id,
            product_name: product.name,
            seller_name: product.seller || "Authorized Merchant",
            base_price: product.price,
            shipping_cost: 0,
            estimated_tax: 0,
            total_cost: product.price,
            estimated_delivery: "2-4 business days"
          });
        })
        .finally(() => setLoadingReview(false));
    }
  }, [isOpen, product]);

  if (!isOpen) return null;

  const handleConfirm = async () => {
    setSubmitting(true);
    try {
      const res = await api.confirmCheckout(
        product.id,
        reviewManifest?.seller_id || "s_default",
        reviewManifest?.total_cost || product.price,
        true
      );
      setResultState(res);
      if (onSuccess) onSuccess(res.external_checkout_url);
    } catch (err: any) {
      alert("Checkout error: " + err.message);
    } finally {
      setSubmitting(false);
    }
  };

  const handleCancel = async () => {
    setSubmitting(true);
    try {
      await api.confirmCheckout(
        product.id,
        reviewManifest?.seller_id || "s_default",
        reviewManifest?.total_cost || product.price,
        false
      );
      onClose();
    } catch {
      onClose();
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm animate-in fade-in duration-200">
      <div className="bg-white rounded-2xl max-w-lg w-full shadow-2xl border border-slate-200 overflow-hidden">
        {/* Header */}
        <div className="bg-amber-500 px-6 py-4 text-white flex items-center justify-between">
          <div className="flex items-center gap-2">
            <AlertTriangle className="w-6 h-6 text-amber-100" />
            <h3 className="font-bold text-lg tracking-tight">HUMAN CONFIRMATION REQUIRED</h3>
          </div>
          <button onClick={onClose} className="p-1 hover:bg-amber-600 rounded-lg transition-colors">
            <X className="w-5 h-5 text-amber-100" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6">
          {resultState ? (
            <div className="text-center py-6">
              <div className="w-14 h-14 rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center mx-auto mb-4">
                <Check className="w-8 h-8" />
              </div>
              <h4 className="text-lg font-bold text-slate-900 mb-2">Purchase Approved by You!</h4>
              <p className="text-sm text-slate-600 mb-6 max-w-sm mx-auto">
                {resultState.message}
              </p>
              {resultState.url && (
                <a
                  href={resultState.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-2 px-5 py-2.5 bg-indigo-600 text-white rounded-xl font-medium shadow-md hover:bg-indigo-700 transition-colors"
                >
                  Proceed to Merchant Checkout <ExternalLink className="w-4 h-4" />
                </a>
              )}
            </div>
          ) : loadingReview ? (
            <div className="py-12 text-center text-slate-500 flex flex-col items-center">
              <Loader2 className="w-8 h-8 animate-spin text-indigo-600 mb-2" />
              <p className="text-sm font-medium">Preparing itemized verification manifest...</p>
            </div>
          ) : (
            <>
              <div className="bg-amber-50/70 border border-amber-200/80 rounded-xl p-3.5 mb-5 text-xs text-amber-900 leading-relaxed flex items-start gap-2.5">
                <ShieldCheck className="w-4 h-4 text-amber-700 shrink-0 mt-0.5" />
                <span>
                  The AI multi-agent assistant never executes autonomous financial deductions. Please carefully review the itemized charges before approving.
                </span>
              </div>

              {/* Itemized Table */}
              <div className="bg-slate-50 rounded-xl p-4 border border-slate-200 divide-y divide-slate-200 text-sm mb-6">
                <div className="pb-3">
                  <span className="text-xs text-slate-500 font-medium block mb-0.5">Product</span>
                  <span className="font-semibold text-slate-900 line-clamp-2">
                    {reviewManifest?.product_name || product.name}
                  </span>
                </div>
                <div className="py-2.5 flex justify-between items-center">
                  <span className="text-slate-600">Merchant / Seller</span>
                  <span className="font-medium text-slate-900">{reviewManifest?.seller_name || product.seller}</span>
                </div>
                <div className="py-2.5 flex justify-between items-center">
                  <span className="text-slate-600">Live Merchant Store Link</span>
                  <a 
                    href={product.url || reviewManifest?.product_url || 'https://www.amazon.in'}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="font-semibold text-indigo-600 hover:text-indigo-800 hover:underline flex items-center gap-1 text-xs truncate max-w-[220px]"
                    title="Open verified store page"
                  >
                    <span>Visit Live Store Page</span>
                    <ExternalLink className="w-3 h-3 shrink-0" />
                  </a>
                </div>
                <div className="py-2.5 flex justify-between items-center">
                  <span className="text-slate-600">Base Price (inclusive of GST)</span>
                  <span className="font-medium text-slate-900">₹{(reviewManifest?.base_price || product.price).toLocaleString()}</span>
                </div>
                <div className="py-2.5 flex justify-between items-center">
                  <span className="text-slate-600">Estimated Shipping</span>
                  <span className="font-medium text-emerald-600">₹{(reviewManifest?.shipping_cost || 0).toLocaleString()} (Free)</span>
                </div>
                <div className="pt-3 flex justify-between items-center font-bold text-base text-slate-900">
                  <span>Total Amount</span>
                  <span className="text-indigo-600 text-lg">
                    ₹{(reviewManifest?.total_cost || product.price).toLocaleString()}
                  </span>
                </div>
              </div>

              <div className="flex items-center gap-2 text-[11px] text-slate-400 mb-6">
                <Lock className="w-3.5 h-3.5" />
                <span>Zero card storage policy: Credit card information is never requested or retained.</span>
              </div>

              {/* Actions */}
              <div className="flex items-center gap-3">
                <button
                  type="button"
                  onClick={handleCancel}
                  disabled={submitting}
                  className="flex-1 px-4 py-2.5 border border-slate-300 rounded-xl font-medium text-slate-700 hover:bg-slate-100 transition-colors"
                >
                  Cancel
                </button>
                <button
                  type="button"
                  onClick={handleConfirm}
                  disabled={submitting}
                  className="flex-1 px-4 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl font-semibold shadow-md shadow-indigo-100 transition-colors flex items-center justify-center gap-1.5"
                >
                  {submitting ? <Loader2 className="w-4 h-4 animate-spin" /> : <Check className="w-4 h-4" />}
                  Confirm Approval
                </button>
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
};
