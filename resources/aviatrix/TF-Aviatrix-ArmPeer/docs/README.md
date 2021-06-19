# TF::Aviatrix::ArmPeer

The **aviatrix_arm_peer** resource allows the creation and management of Aviatrix ARM peerings.

!> **WARNING:** The `aviatrix_arm_peer` resource is deprecated as of **Release 2.12**. It is currently kept for backward-compatibility and will be removed in the future. Please use the Azure peer resource instead. If this is already in the state, please remove it from the state file and import as `aviatrix_azure_peer`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::ArmPeer",
    "Properties" : {
        "<a href="#accountname1" title="AccountName1">AccountName1</a>" : <i>String</i>,
        "<a href="#accountname2" title="AccountName2">AccountName2</a>" : <i>String</i>,
        "<a href="#vnetnameresourcegroup1" title="VnetNameResourceGroup1">VnetNameResourceGroup1</a>" : <i>String</i>,
        "<a href="#vnetnameresourcegroup2" title="VnetNameResourceGroup2">VnetNameResourceGroup2</a>" : <i>String</i>,
        "<a href="#vnetreg1" title="VnetReg1">VnetReg1</a>" : <i>String</i>,
        "<a href="#vnetreg2" title="VnetReg2">VnetReg2</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::ArmPeer
Properties:
    <a href="#accountname1" title="AccountName1">AccountName1</a>: <i>String</i>
    <a href="#accountname2" title="AccountName2">AccountName2</a>: <i>String</i>
    <a href="#vnetnameresourcegroup1" title="VnetNameResourceGroup1">VnetNameResourceGroup1</a>: <i>String</i>
    <a href="#vnetnameresourcegroup2" title="VnetNameResourceGroup2">VnetNameResourceGroup2</a>: <i>String</i>
    <a href="#vnetreg1" title="VnetReg1">VnetReg1</a>: <i>String</i>
    <a href="#vnetreg2" title="VnetReg2">VnetReg2</a>: <i>String</i>
</pre>

## Properties

#### AccountName1

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountName2

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetNameResourceGroup1

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetNameResourceGroup2

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetReg1

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnetReg2

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### VnetCidr1

Returns the <code>VnetCidr1</code> value.

#### VnetCidr2

Returns the <code>VnetCidr2</code> value.

