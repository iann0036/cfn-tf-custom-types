# Terraform::AWS::OpsworksMemcachedLayer EbsVolume

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>Boolean</i>,
    "<a href="#iops" title="Iops">Iops</a>" : <i>Double</i>,
    "<a href="#mountpoint" title="MountPoint">MountPoint</a>" : <i>String</i>,
    "<a href="#numberofdisks" title="NumberOfDisks">NumberOfDisks</a>" : <i>Double</i>,
    "<a href="#raidlevel" title="RaidLevel">RaidLevel</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#encrypted" title="Encrypted">Encrypted</a>: <i>Boolean</i>
<a href="#iops" title="Iops">Iops</a>: <i>Double</i>
<a href="#mountpoint" title="MountPoint">MountPoint</a>: <i>String</i>
<a href="#numberofdisks" title="NumberOfDisks">NumberOfDisks</a>: <i>Double</i>
<a href="#raidlevel" title="RaidLevel">RaidLevel</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Encrypted

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Iops

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountPoint

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumberOfDisks

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RaidLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

