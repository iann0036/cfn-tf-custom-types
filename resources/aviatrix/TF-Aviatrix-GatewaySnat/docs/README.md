# TF::Aviatrix::GatewaySnat

The **aviatrix_gateway_snat** resource configures and manages policies for customized source NAT for Aviatrix gateways.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::GatewaySnat",
    "Properties" : {
        "<a href="#gwname" title="GwName">GwName</a>" : <i>String</i>,
        "<a href="#snatmode" title="SnatMode">SnatMode</a>" : <i>String</i>,
        "<a href="#synctoha" title="SyncToHa">SyncToHa</a>" : <i>Boolean</i>,
        "<a href="#snatpolicy" title="SnatPolicy">SnatPolicy</a>" : <i>[ <a href="snatpolicydefinition.md">SnatPolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::GatewaySnat
Properties:
    <a href="#gwname" title="GwName">GwName</a>: <i>String</i>
    <a href="#snatmode" title="SnatMode">SnatMode</a>: <i>String</i>
    <a href="#synctoha" title="SyncToHa">SyncToHa</a>: <i>Boolean</i>
    <a href="#snatpolicy" title="SnatPolicy">SnatPolicy</a>: <i>
      - <a href="snatpolicydefinition.md">SnatPolicyDefinition</a></i>
</pre>

## Properties

#### GwName

Name of the Aviatrix gateway the custom SNAT will be configured for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatMode

NAT mode. Valid values: "customized_snat". Default value: "customized_snat".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncToHa

Sync the policies to the HA gateway. Valid values: true, false. Default: false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatPolicy

_Required_: No

_Type_: List of <a href="snatpolicydefinition.md">SnatPolicyDefinition</a>

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

