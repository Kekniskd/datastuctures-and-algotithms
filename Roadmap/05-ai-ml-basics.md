# 05 · AI/ML basics

← [[README]] · Hours: ~45 · Phases 1–2, feeding into [[06-llm-genai]]

Goal calibration: unless you're targeting an ML-engineer role, you need **fluent fundamentals + one ML systems design framework**, not research depth. That's enough to pass an ML-adjacent screen, hold your own in a Google team match with an ML team, and make [[06-llm-genai]] actually make sense instead of being cargo-cult.

---

## 1. Math floor (2 weeks, don't over-invest)

- **Linear algebra:** vectors, dot product (= similarity), matrix multiplication shapes, transpose, identity/inverse, rank, eigenvectors (for PCA), norms (L1/L2), cosine similarity. If you can hand-multiply a (2×3)(3×2) and say what the dot product *means*, you're set.
- **Probability & stats:** conditional probability, Bayes' rule, independence, expectation/variance, distributions (Bernoulli, binomial, normal, Poisson, exponential), CLT, law of large numbers, MLE, sampling bias, confidence intervals, hypothesis testing, p-values, **statistical power** (needed for A/B tests).
- **Calculus:** derivative as slope, partial derivatives, gradient, chain rule (= backprop), convexity, local vs global minima. Nothing more.
- **Information theory:** entropy, cross-entropy, KL divergence — you need these for loss functions and for [[06-llm-genai]].

---

## 2. Core ML concepts (the interview backbone)

- **Learning types:** supervised, unsupervised, semi-supervised, self-supervised (← how LLMs are trained), reinforcement learning.
- **The generalization story:** underfitting vs overfitting, **bias–variance decomposition**, train/validation/test splits, k-fold cross-validation, learning curves, why you never touch the test set twice.
- **Regularization:** L1 (sparsity/feature selection) vs L2 (shrinkage), elastic net, dropout, early stopping, data augmentation, weight decay, label smoothing.
- **Loss functions and when:** MSE/MAE/Huber (regression), binary & categorical cross-entropy, hinge, focal loss (imbalance), contrastive/triplet (embeddings), ranking losses (pairwise/listwise).
- **Optimization:** gradient descent → SGD → mini-batch; momentum, RMSProp, **Adam/AdamW**; learning-rate schedules (warmup, cosine decay); batch size effects; vanishing/exploding gradients; gradient clipping.
- **Evaluation — know the tradeoffs cold:** accuracy (and why it's useless at 1% positives), precision/recall, F1, PR curve vs ROC-AUC (PR for imbalanced), confusion matrix, threshold selection driven by business cost, calibration, log loss; ranking metrics (MAP, MRR, **NDCG**, recall@k); regression (RMSE, MAE, R²).
- **Data problems (where real interviews go):** class imbalance (resampling, SMOTE, class weights, threshold tuning), **data leakage** (the #1 real-world bug — target leakage, temporal leakage, leakage via preprocessing before splitting), missing values, outliers, label noise, train/serve skew, sampling for a time-series problem (never random-split time series).
- **Feature engineering:** scaling/normalization, one-hot vs target vs hash encoding, binning, interactions, log transforms, embeddings for high-cardinality categoricals, temporal features, feature stores, feature selection (mutual information, permutation importance, SHAP).
- **Interpretability:** feature importance, SHAP/LIME, partial dependence; why a bank uses logistic regression over XGBoost.
- **Ethics/practical:** bias in data, fairness metrics (demographic parity vs equal opportunity), privacy (PII, differential privacy, federated learning), model cards.

---

## 3. Classical algorithms — know the assumption, cost, and failure mode of each

| Algorithm | Key idea | When it wins | Watch out |
|---|---|---|---|
| Linear regression | Least squares | Interpretable baseline | Assumes linearity, sensitive to outliers |
| Logistic regression | Log-odds + sigmoid | Strong baseline, calibrated probabilities | Needs feature engineering |
| Decision tree | Recursive splits (Gini/entropy) | Interpretable, non-linear, no scaling needed | Overfits; unstable |
| Random forest | Bagging + feature subsampling | Robust default, low tuning | Big models, weaker on ranking |
| **Gradient boosting (XGBoost/LightGBM)** | Fit residuals sequentially | **The winner on tabular data** | Overfits without early stopping; tuning cost |
| SVM | Max-margin + kernel trick | Small data, high dimensions | Poor scaling to big N |
| kNN | Instance-based | Simple baseline, recommender-ish | Slow at inference, curse of dimensionality |
| Naive Bayes | Conditional independence | Text baselines, tiny/fast | Independence assumption is false |
| k-means | Centroid minimization | Fast clustering | Must pick k; assumes spherical clusters |
| Hierarchical / DBSCAN | Linkage / density | Arbitrary shapes, outlier detection | Parameters, scale |
| PCA | Variance-maximizing projection | Dimensionality reduction, visualization | Linear only; interpretability loss |
| Matrix factorization / ALS | Latent factors | Collaborative filtering | Cold start |

Say "I'd start with a heuristic baseline, then logistic regression, then gradient boosting" — starting simple is a graded signal.

---

## 4. Deep learning essentials

- **MLP + backprop:** derive the gradients for a 2-layer net once, by hand. This single exercise unlocks everything in [[06-llm-genai]].
- Activations: sigmoid/tanh (saturation), **ReLU** (dead units), LeakyReLU, **GELU/SwiGLU** (what transformers use).
- Initialization (Xavier/He) and why it matters; normalization: **batch norm vs layer norm** (and why transformers use layer/RMS norm — sequence-length independence, small batches).
- Residual connections — why depth needs them.
- Regularization in DL: dropout, weight decay, augmentation, early stopping.
- **CNNs:** convolution, kernels, stride/padding, pooling, receptive field, parameter sharing, translation invariance, transfer learning and fine-tuning.
- **Sequences:** RNN → vanishing gradients → LSTM/GRU (gates) → why attention replaced them (parallelism + long-range dependencies). This is the bridge into transformers.
- **Embeddings:** word2vec (skip-gram, negative sampling), GloVe, contextual embeddings, embedding arithmetic, cosine similarity, ANN search (HNSW, IVF, PQ) — directly reused in RAG.
- Training practicalities: GPU/TPU basics, mixed precision, gradient accumulation, checkpointing, distributed training (data vs model vs pipeline parallel), hyperparameter search (random > grid; Bayesian/Optuna).

---

## 5. Tools

`numpy` (broadcasting, vectorization — no Python loops), `pandas` (groupby, merge, pivot, time series), `scikit-learn` (`Pipeline`, `ColumnTransformer`, `cross_val_score`, `GridSearchCV` — use pipelines to avoid leakage), `matplotlib`/`seaborn`, **`pytorch`** (tensors, autograd, `nn.Module`, `DataLoader`, training loop written from scratch at least twice), plus `xgboost`/`lightgbm`. Awareness only: MLflow/W&B, Airflow, BigQuery, Vertex AI, TFX.

**Do these four projects (small, complete, in the repo):**
1. Tabular end-to-end: EDA → pipeline → GBM → cross-validated metric → error analysis writeup.
2. Train an MLP on MNIST in raw PyTorch with a hand-written training loop.
3. Text classifier: TF-IDF + logistic regression baseline, then embeddings + fine-tune. Compare honestly.
4. A tiny recommender (matrix factorization or item-item kNN) with recall@k and NDCG.

---

## 6. ML systems design (the round that actually exists)

If you interview for anything ML-adjacent, this replaces or supplements the [[04-hld]] round. The framework:

1. **Clarify the business objective**, then translate it to an ML objective and a metric. ("Increase watch time" → "predict P(click) and P(watch>30s)"; state the proxy-metric risk.)
2. **Is ML even the right tool?** Baseline heuristic first — say this out loud.
3. **Data:** sources, labels (explicit vs implicit feedback), volume, freshness, privacy, label delay, negative sampling strategy.
4. **Features:** user / item / context / interaction / temporal. Discuss the feature store and training-serving consistency.
5. **Model:** baseline → candidate models → why. For retrieval+ranking problems, the standard two-stage (or three-stage) architecture: **candidate generation (recall, cheap, millions→hundreds) → ranking (precision, expensive) → re-ranking (diversity, business rules, freshness)**.
6. **Training:** offline batch, incremental, online learning; retraining cadence and its trigger; cold start (new user/new item); positional/selection bias.
7. **Evaluation:** offline metrics (and their disagreement with online), **A/B testing** (hypothesis, randomization unit, sample size/power, novelty effect, guardrail metrics), interleaving, shadow deployment, holdback.
8. **Serving:** batch vs real-time, latency budget (e.g. 100 ms p99 → hard constraint on model size), embedding ANN index, model server, caching predictions, fallbacks when the model is down.
9. **Monitoring:** data drift, concept drift, feature-pipeline failures, prediction distribution shifts, feedback loops (the model teaches itself its own bias), on-call for models.

**Practice problems:** YouTube/Netflix recommendations · Google Ads CTR prediction · search ranking · news feed ranking · fraud/spam detection · Gmail smart-reply · Photos similarity search · ETA prediction · content moderation · dynamic pricing · churn prediction · Google Lens style visual search.

---

## 7. Question bank

1. Explain bias–variance with a concrete example of each failure.
2. Model gets 99% accuracy on fraud detection. What's your reaction?
3. Precision vs recall for cancer screening vs spam filtering — which do you optimize and why?
4. ROC-AUC vs PR-AUC for 0.1% positives?
5. Your validation score is great, production is terrible. Give 6 hypotheses in priority order.
6. What is data leakage? Name three ways it sneaks in.
7. Why is random train/test split wrong for time-series?
8. L1 vs L2: which zeroes out features, and why geometrically?
9. Why does Adam usually beat plain SGD — and when doesn't it?
10. Explain backprop for a 2-layer network in 90 seconds.
11. Batch norm vs layer norm; why do transformers pick one?
12. How do you handle a 1000-category feature?
13. Cold start for a new user in a recommender — three approaches.
14. How do you size an A/B test, and what's a guardrail metric?
15. Offline metric improved, online metric didn't. What now?
16. How would you detect drift in production without labels?
17. When do you choose a simpler model on purpose?
18. Latency budget is 50 ms and your best model takes 300 ms. Options?
19. Explain the two-stage retrieval-and-ranking architecture and why not just rank everything.
20. Your training data comes from your own model's past recommendations. What's the problem?
