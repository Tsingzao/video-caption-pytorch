import torch.nn as nn


class Vid2seq(nn.Module):
    def __init__(self, encoder, decoder):
        """

        Args:
            encoder (nn.Module): Encoder rnn
            decoder (nn.Module): Decoder rnn
        """
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder

    def flatten_parameters(self):
        self.encoder.rnn.flatten_parameters()
        self.decoder.rnn.flatten_parameters()

    def forward(self, vid_feats, target_variable=None,
                teacher_forcing_ratio=1):
        """

        Args:
            vid_feats (Variable): Description
            input_lengths (None, optional): Description
            target_variable (None, optional): Description
            teacher_forcing_ratio (int, optional): Description

        Returns:
            TYPE: Description
        """
        encoder_outputs, encoder_hidden = self.encoder(vid_feats)
        seq_prob, seq_preds = self.decoder(encoder_hidden=encoder_hidden,
                                           encoder_outputs=encoder_outputs,
                                           targets=target_variable,
                                           teacher_forcing_ratio=teacher_forcing_ratio)
        return seq_prob, seq_preds
