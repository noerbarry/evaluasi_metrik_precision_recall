import streamlit as st
import pandas as pd
from sklearn.metrics import precision_score, recall_score

def calculate_metrics(y_true, y_pred, categories):
    metrics = {}

    for category in categories:
        true_indices = [i for i, label in enumerate(y_true) if label == category]
        pred_indices = [i for i, label in enumerate(y_pred) if label == category]

        true_labels = [1 if i in true_indices else 0 for i in range(len(y_true))]
        pred_labels = [1 if i in pred_indices else 0 for i in range(len(y_pred))]

        precision = precision_score(true_labels, pred_labels)
        recall = recall_score(true_labels, pred_labels)

        metrics[category] = {'Precision': precision, 'Recall': recall}

    return metrics

def main():
    st.title('PABAR Precision & Recall Calculator')

    uploaded_file = st.file_uploader("Upload file (XLSX or CSV)", type=["xlsx", "csv"])
    
    if uploaded_file is not None:
        try:
            data = pd.read_excel(uploaded_file) if uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" else pd.read_csv(uploaded_file)
            
            st.write("Uploaded Data:")
            st.write(data)
            
            y_true = data['Ground Truth'].tolist()
            y_pred = data['Prediction'].tolist()

            categories = list(set(y_true))  # Menggunakan label unik dari Ground Truth sebagai kategori
            
            metrics = calculate_metrics(y_true, y_pred, categories)
            
            st.write("Metrics:")
            for category, values in metrics.items():
                st.write(f"Category: {category}")
                st.write(f"Precision: {values['Precision']:.2f}")
                st.write(f"Recall: {values['Recall']:.2f}")
                st.write("---")
        except Exception as e:
            st.write("Error occurred:", e)

if __name__ == "__main__":
    main()
