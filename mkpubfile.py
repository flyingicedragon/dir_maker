#!/usr/bin/env python
import maker

maker.parser.add_argument(
    '-p',
    '--permission',
    type=str,
    default='774',
    help='Permission of dir. Permission must be descriped by number. Default is 744'
)
args = maker.parser.parse_args()
maker.make_file(args.name, args.permission, args.group)
