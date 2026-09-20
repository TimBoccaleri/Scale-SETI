#!/usr/bin/env python3
import argparse, json
import pandas as pd

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--trials',required=True)
    ap.add_argument('--out',required=True)
    ap.add_argument('--summary',required=True)
    a=ap.parse_args()
    df=pd.read_csv(a.trials, dtype={'challenge_bits': str, 'decoded_response': str})
    df['recalc_hamming']=[sum(x!=y for x,y in zip(a,b)) for a,b in zip(df.challenge_bits,df.decoded_response)]
    if not (df.recalc_hamming==df.hamming_distance).all():
        raise SystemExit('Hamming mismatch in source data')
    grouped=df.groupby('condition_code').agg(trials=('trial_id','count'),mean_hamming=('hamming_distance','mean'),median_hamming=('hamming_distance','median'),exact_matches=('exact_match','sum'),mean_bit_accuracy=('bit_accuracy','mean'),mean_correlation=('receiver_correlation','mean'),telemetry_flags=('telemetry_flag','sum')).reset_index()
    grouped.to_csv(a.out,index=False)
    pos=df[df.condition_code=='POSITIVE']
    controls=df[df.condition_code!='POSITIVE']
    summary={
      'trial_count':int(len(df)),
      'positive_mean_bit_accuracy':float(pos.bit_accuracy.mean()),
      'positive_exact_matches':int(pos.exact_match.sum()),
      'control_mean_bit_accuracy':float(controls.bit_accuracy.mean()),
      'control_exact_matches':int(controls.exact_match.sum()),
      'sanity_pass':bool(pos.bit_accuracy.mean()>0.98 and abs(controls.bit_accuracy.mean()-0.5)<0.08)
    }
    with open(a.summary,'w') as f: json.dump(summary,f,indent=2)
    print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
