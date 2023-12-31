# Main domain adaptive fine-tuning
TRAIN_ESNLI=data/esnli/esnli.train.highlight.contradiction.jsonl
EVAL_ESNLI=data/esnli/esnli.dev.highlight.contradiction.jsonl
TRAIN_FIN10K=data/fin10k/fin10k.heuristic.synthetic.balance.train.type2.jsonl
TRAIN_FIN10K_SOFT=data/fin10k/fin10k.heuristic.synthetic.balance.soft.train.type2.jsonl
TRAIN_FIN10K_LEXICON=data/fin10k/fin10k.lexicon.synthetic.balance.train.type2.jsonl

export CUDA_VISIBLE_DEVICES=0

# Setting Zero-shot
TYPE=esnli-zs-highlighter
BS=24
python3 train.py \
  --model_name_or_path bert-base-uncased \
  --config_name bert-base-uncased \
  --output_dir checkpoints/$TYPE \
  --train_file $TRAIN_ESNLI \
  --eval_file $EVAL_ESNLI \
  --per_device_train_batch_size $BS \
  --max_steps 15000 \
  --save_steps 5000 \
  --eval_steps 5000 \
  --max_seq_length 258 \
  --evaluation_strategy 'steps'\
  --evaluate_during_training \
  --do_train \
  --do_eval

# Setting from-scratch
TYPE=from-scratch
BS=24
python3 train.py \
  --model_name_or_path bert-base-uncased \
  --config_name bert-base-uncased \
  --output_dir checkpoints/$TYPE \
  --train_file $TRAIN_FIN10K \
  --eval_file $EVAL_ESNLI \
  --per_device_train_batch_size $BS \
  --max_steps 10000 \
  --save_steps 1500 \
  --eval_steps 1500 \
  --max_seq_length 512 \
  --evaluation_strategy 'steps'\
  --evaluate_during_training \
  --soft_labeling false  \
  --tau 1 \
  --gamma 1 \
  --do_train \
  --do_eval

# Setting soft-labeling (hard)
TYPE=further-finetune
BS=24 
python3 train.py \
  --ignore_data_skip \
  --resume_from_checkpoint checkpoints/esnli-zs-highlighter/checkpoint-15000 \
  --model_name_or_path bert-base-uncased \
  --config_name bert-base-uncased \
  --output_dir checkpoints/$TYPE \
  --train_file $TRAIN_FIN10K \
  --eval_file $EVAL_ESNLI \
  --per_device_train_batch_size $BS \
  --max_steps 20000\
  --save_steps 1500 \
  --eval_steps 1500 \
  --max_seq_length 512 \
  --evaluation_strategy 'steps'\
  --evaluate_during_training \
  --soft_labeling false  \
  --tau 1 \
  --gamma 1 \
  --do_train \
  --do_eval 


# Setting soft-labeling (balance)
TYPE=further-finetune-sl-balance # tau=1, gamma=0.5
BS=24
python3 train.py \
  --resume_from_checkpoint checkpoints/esnli-zs-highlighter/checkpoint-15000 \
  --model_name_or_path bert-base-uncased \
  --config_name bert-base-uncased \
  --output_dir checkpoints/$TYPE \
  --train_file $TRAIN_FIN10K_SOFT \
  --eval_file $EVAL_ESNLI \
  --per_device_train_batch_size $BS \
  --max_steps 20000 \
  --save_steps 1500 \
  --eval_steps 1500 \
  --max_seq_length 512 \
  --evaluation_strategy 'steps'\
  --evaluate_during_training \
  --soft_labeling true  \
  --tau 1 \
  --gamma 0.5 \
  --do_train \
  --do_eval

# Setting soft-labeling (tunned)
TYPE=further-finetun-sl-tunned # tau=1, gamma=0.1
BS=24
python3 train.py \
  --resume_from_checkpoint checkpoints/esnli-zs-highlighter/checkpoint-15000 \
  --model_name_or_path bert-base-uncased \
  --config_name bert-base-uncased \
  --output_dir checkpoints/$TYPE \
  --train_file $TRAIN_FIN10K_SOFT \
  --eval_file $EVAL_ESNLI \
  --per_device_train_batch_size $BS \
  --max_steps 20000 \
  --save_steps 1500 \
  --eval_steps 1500 \
  --max_seq_length 512 \
  --evaluation_strategy 'steps'\
  --evaluate_during_training \
  --soft_labeling true  \
  --tau 1 \
  --gamma 0.1 \
  --do_train \
  --do_eval

# Setting soft-labeling (soft)
TYPE=further-finetune-soft # tau=1, gamma=0
BS=24
python3 train.py \
  --resume_from_checkpoint checkpoints/esnli-zs-highlighter/checkpoint-15000 \
  --model_name_or_path bert-base-uncased \
  --output_dir checkpoints/$TYPE \
  --train_file $TRAIN_FIN10K_SOFT \
  --eval_file $EVAL_ESNLI \
  --per_device_train_batch_size $BS \
  --max_steps 20000 \
  --save_steps 1500 \
  --eval_steps 1500 \
  --max_seq_length 512 \
  --evaluation_strategy 'steps'\
  --evaluate_during_training \
  --soft_labeling true  \
  --tau 1 \
  --gamma 0 \
  --do_train \
  --do_eval

