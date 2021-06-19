# TF::Aviatrix::FirewallManagementAccess

The **aviatrix_firewall_management_access** resource allows the management of which resource to permit visibility into the Transit (FireNet) VPC.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::FirewallManagementAccess",
    "Properties" : {
        "<a href="#managementaccessresourcename" title="ManagementAccessResourceName">ManagementAccessResourceName</a>" : <i>String</i>,
        "<a href="#transitfirenetgatewayname" title="TransitFirenetGatewayName">TransitFirenetGatewayName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::FirewallManagementAccess
Properties:
    <a href="#managementaccessresourcename" title="ManagementAccessResourceName">ManagementAccessResourceName</a>: <i>String</i>
    <a href="#transitfirenetgatewayname" title="TransitFirenetGatewayName">TransitFirenetGatewayName</a>: <i>String</i>
</pre>

## Properties

#### ManagementAccessResourceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitFirenetGatewayName

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

