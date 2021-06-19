# TF::CheckPoint::ManagementCheckpointHost InterfacesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#color" title="Color">Color</a>" : <i>String</i>,
    "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
    "<a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>" : <i>Boolean</i>,
    "<a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>" : <i>Boolean</i>,
    "<a href="#masklength4" title="MaskLength4">MaskLength4</a>" : <i>Double</i>,
    "<a href="#masklength6" title="MaskLength6">MaskLength6</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#subnet4" title="Subnet4">Subnet4</a>" : <i>String</i>,
    "<a href="#subnet6" title="Subnet6">Subnet6</a>" : <i>String</i>,
    "<a href="#subnetmask" title="SubnetMask">SubnetMask</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#color" title="Color">Color</a>: <i>String</i>
<a href="#comments" title="Comments">Comments</a>: <i>String</i>
<a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>: <i>Boolean</i>
<a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>: <i>Boolean</i>
<a href="#masklength4" title="MaskLength4">MaskLength4</a>: <i>Double</i>
<a href="#masklength6" title="MaskLength6">MaskLength6</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#subnet4" title="Subnet4">Subnet4</a>: <i>String</i>
<a href="#subnet6" title="Subnet6">Subnet6</a>: <i>String</i>
<a href="#subnetmask" title="SubnetMask">SubnetMask</a>: <i>String</i>
</pre>

## Properties

#### Color

Color of the object. Should be one of existing colors.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comments string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreErrors

Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreWarnings

Apply changes ignoring warnings.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaskLength4

IPv4 network mask length.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaskLength6

IPv6 network mask length.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Interface name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet4

IPv4 network address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet6

IPv6 network address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetMask

IPv4 network mask.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

