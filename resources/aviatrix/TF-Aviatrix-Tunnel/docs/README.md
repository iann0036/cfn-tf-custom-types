# TF::Aviatrix::Tunnel

The **aviatrix_tunnel** resource allows the creation and management of Aviatrix Encrypted Peering tunnels.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::Tunnel",
    "Properties" : {
        "<a href="#enableha" title="EnableHa">EnableHa</a>" : <i>Boolean</i>,
        "<a href="#gwname1" title="GwName1">GwName1</a>" : <i>String</i>,
        "<a href="#gwname2" title="GwName2">GwName2</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::Tunnel
Properties:
    <a href="#enableha" title="EnableHa">EnableHa</a>: <i>Boolean</i>
    <a href="#gwname1" title="GwName1">GwName1</a>: <i>String</i>
    <a href="#gwname2" title="GwName2">GwName2</a>: <i>String</i>
</pre>

## Properties

#### EnableHa

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GwName1

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GwName2

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

#### PeeringHastatus

Returns the <code>PeeringHastatus</code> value.

#### PeeringLink

Returns the <code>PeeringLink</code> value.

#### PeeringState

Returns the <code>PeeringState</code> value.

