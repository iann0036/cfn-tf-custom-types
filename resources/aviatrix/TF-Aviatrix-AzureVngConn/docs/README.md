# TF::Aviatrix::AzureVngConn

The **aviatrix_azure_vng_conn** resource allows the creation and management of the connection between Aviatrix Transit Gateway and Azure VNG.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::AzureVngConn",
    "Properties" : {
        "<a href="#connectionname" title="ConnectionName">ConnectionName</a>" : <i>String</i>,
        "<a href="#primarygatewayname" title="PrimaryGatewayName">PrimaryGatewayName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::AzureVngConn
Properties:
    <a href="#connectionname" title="ConnectionName">ConnectionName</a>: <i>String</i>
    <a href="#primarygatewayname" title="PrimaryGatewayName">PrimaryGatewayName</a>: <i>String</i>
</pre>

## Properties

#### ConnectionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryGatewayName

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

#### Attached

Returns the <code>Attached</code> value.

#### Id

Returns the <code>Id</code> value.

#### VngName

Returns the <code>VngName</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

