# TF::AWS::TransferUser PosixProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#gid" title="Gid">Gid</a>" : <i>Double</i>,
    "<a href="#secondarygids" title="SecondaryGids">SecondaryGids</a>" : <i>[ Double, ... ]</i>,
    "<a href="#uid" title="Uid">Uid</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#gid" title="Gid">Gid</a>: <i>Double</i>
<a href="#secondarygids" title="SecondaryGids">SecondaryGids</a>: <i>
      - Double</i>
<a href="#uid" title="Uid">Uid</a>: <i>Double</i>
</pre>

## Properties

#### Gid

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryGids

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uid

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

