# TF::Akamai::AppsecSecurityPolicyProtections

Use the `akamai_appsec_security_policy_protections` resource to create or modify ...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::AppsecSecurityPolicyProtections",
    "Properties" : {
        "<a href="#applyapiconstraints" title="ApplyApiConstraints">ApplyApiConstraints</a>" : <i>Boolean</i>,
        "<a href="#applyapplicationlayercontrols" title="ApplyApplicationLayerControls">ApplyApplicationLayerControls</a>" : <i>Boolean</i>,
        "<a href="#applybotmancontrols" title="ApplyBotmanControls">ApplyBotmanControls</a>" : <i>Boolean</i>,
        "<a href="#applynetworklayercontrols" title="ApplyNetworkLayerControls">ApplyNetworkLayerControls</a>" : <i>Boolean</i>,
        "<a href="#applyratecontrols" title="ApplyRateControls">ApplyRateControls</a>" : <i>Boolean</i>,
        "<a href="#applyreputationcontrols" title="ApplyReputationControls">ApplyReputationControls</a>" : <i>Boolean</i>,
        "<a href="#applyslowpostcontrols" title="ApplySlowPostControls">ApplySlowPostControls</a>" : <i>Boolean</i>,
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>Double</i>,
        "<a href="#securitypolicyid" title="SecurityPolicyId">SecurityPolicyId</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::AppsecSecurityPolicyProtections
Properties:
    <a href="#applyapiconstraints" title="ApplyApiConstraints">ApplyApiConstraints</a>: <i>Boolean</i>
    <a href="#applyapplicationlayercontrols" title="ApplyApplicationLayerControls">ApplyApplicationLayerControls</a>: <i>Boolean</i>
    <a href="#applybotmancontrols" title="ApplyBotmanControls">ApplyBotmanControls</a>: <i>Boolean</i>
    <a href="#applynetworklayercontrols" title="ApplyNetworkLayerControls">ApplyNetworkLayerControls</a>: <i>Boolean</i>
    <a href="#applyratecontrols" title="ApplyRateControls">ApplyRateControls</a>: <i>Boolean</i>
    <a href="#applyreputationcontrols" title="ApplyReputationControls">ApplyReputationControls</a>: <i>Boolean</i>
    <a href="#applyslowpostcontrols" title="ApplySlowPostControls">ApplySlowPostControls</a>: <i>Boolean</i>
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>Double</i>
    <a href="#securitypolicyid" title="SecurityPolicyId">SecurityPolicyId</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
</pre>

## Properties

#### ApplyApiConstraints

Whether to enable api constraints: either `true` or `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplyApplicationLayerControls

Whether to enable application layer controls: either `true` or `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplyBotmanControls

Whether to enable botman controls: either `true` or `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplyNetworkLayerControls

Whether to enable network layer controls: either `true` or `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplyRateControls

Whether to enable rate controls: either `true` or `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplyReputationControls

Whether to enable reputation controls: either `true` or `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplySlowPostControls

Whether to enable slow post controls: either `true` or `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigId

The ID of the security configuration to use.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityPolicyId

The ID of the security policy to use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The version number of the security configuration to use.

_Required_: Yes

_Type_: Double

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

