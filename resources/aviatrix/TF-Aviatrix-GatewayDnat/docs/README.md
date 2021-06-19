# TF::Aviatrix::GatewayDnat

The **aviatrix_gateway_dnat** resource configures and manages policies for destination NAT function for Aviatrix gateways.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::GatewayDnat",
    "Properties" : {
        "<a href="#gwname" title="GwName">GwName</a>" : <i>String</i>,
        "<a href="#synctoha" title="SyncToHa">SyncToHa</a>" : <i>Boolean</i>,
        "<a href="#dnatpolicy" title="DnatPolicy">DnatPolicy</a>" : <i>[ <a href="dnatpolicydefinition.md">DnatPolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::GatewayDnat
Properties:
    <a href="#gwname" title="GwName">GwName</a>: <i>String</i>
    <a href="#synctoha" title="SyncToHa">SyncToHa</a>: <i>Boolean</i>
    <a href="#dnatpolicy" title="DnatPolicy">DnatPolicy</a>: <i>
      - <a href="dnatpolicydefinition.md">DnatPolicyDefinition</a></i>
</pre>

## Properties

#### GwName

Name of the Aviatrix gateway the custom DNAT will be configured for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncToHa

Sync the policies to the HA gateway. Valid values: true, false. Default: true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnatPolicy

_Required_: No

_Type_: List of <a href="dnatpolicydefinition.md">DnatPolicyDefinition</a>

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

