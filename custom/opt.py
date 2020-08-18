opt = {
        "no_cuda": True,
        "task": "internal:blended_skill_talk,wizard_of_wikipedia,convai2,empathetic_dialogues",
        "multitask_weights": [
            1.0,
            3.0,
            3.0,
            3.0
        ],
        "init_model": "./data/models/blender/blender_90M/model",
        "dict_file":"./data/models/blender/blender_90M/model.dict",
        "embedding_size": 512,
        "n_layers": 8,
        "ffn_size": 2048,
        "dropout": 0.1,
        "n_heads": 16,
        "learn_positional_embeddings": True,
        "n_positions": 512,
        'variant': 'xlm',
        'activation': 'gelu',
        'skip_generation': True,
        'fp16': True,
        'text-truncate': 512,
        'label_truncate': 128,
        'dict_tokenizer': 'bpe',
        'dict_lower': True,
        'lr': 1e-06,
        'optimizer': 'adamax',
        'lr_scheduler': 'reduceonplateau',
        'gradient_clip': 0.1,
        'veps': 0.25,
        "betas": [
            0.9,
            0.999
        ],        
        "update_freq": 1,
        "attention_dropout": 0.0,
        "relu_dropout": 0.0,
        "skip_generation": False,
        'vp': 15,
        'stim': 60,
        'vme': 20000,
        'bs': 16,
        'vmt': 'ppl',
        'vmm': 'min',
        'save_after_valid': True,
        'model_file': '/tmp/test_train_90M',
        'datapath': './custom/data/',        
        'history_size': -1,
        'truncate': -1,
        'rank_candidates': False,
        'embeddings_scale': True,
        'output_scaling': 1.0,
        'embedding_type': 'random',
        'gpu': -1
    }
