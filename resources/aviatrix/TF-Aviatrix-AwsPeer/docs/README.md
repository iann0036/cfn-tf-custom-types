# TF::Aviatrix::AwsPeer

The **aviatrix_aws_peer** resource allows the creation and management of Aviatrix-created native AWS intra and inter-region VPC peerings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::AwsPeer",
    "Properties" : {
        "<a href="#accountname1" title="AccountName1">AccountName1</a>" : <i>String</i>,
        "<a href="#accountname2" title="AccountName2">AccountName2</a>" : <i>String</i>,
        "<a href="#rtblist1" title="RtbList1">RtbList1</a>" : <i>[ String, ... ]</i>,
        "<a href="#rtblist2" title="RtbList2">RtbList2</a>" : <i>[ String, ... ]</i>,
        "<a href="#vpcid1" title="VpcId1">VpcId1</a>" : <i>String</i>,
        "<a href="#vpcid2" title="VpcId2">VpcId2</a>" : <i>String</i>,
        "<a href="#vpcreg1" title="VpcReg1">VpcReg1</a>" : <i>String</i>,
        "<a href="#vpcreg2" title="VpcReg2">VpcReg2</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::AwsPeer
Properties:
    <a href="#accountname1" title="AccountName1">AccountName1</a>: <i>String</i>
    <a href="#accountname2" title="AccountName2">AccountName2</a>: <i>String</i>
    <a href="#rtblist1" title="RtbList1">RtbList1</a>: <i>
      - String</i>
    <a href="#rtblist2" title="RtbList2">RtbList2</a>: <i>
      - String</i>
    <a href="#vpcid1" title="VpcId1">VpcId1</a>: <i>String</i>
    <a href="#vpcid2" title="VpcId2">VpcId2</a>: <i>String</i>
    <a href="#vpcreg1" title="VpcReg1">VpcReg1</a>: <i>String</i>
    <a href="#vpcreg2" title="VpcReg2">VpcReg2</a>: <i>String</i>
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

#### RtbList1

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RtbList2

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId1

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId2

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcReg1

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcReg2

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

#### RtbList1Output

Returns the <code>RtbList1Output</code> value.

#### RtbList2Output

Returns the <code>RtbList2Output</code> value.

