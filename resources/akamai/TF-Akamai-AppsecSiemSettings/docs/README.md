# TF::Akamai::AppsecSiemSettings

Use the `akamai_appsec_siem_settings` resource to mpdate the SIEM integration settings for a specific configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::AppsecSiemSettings",
    "Properties" : {
        "<a href="#configid" title="ConfigId">ConfigId</a>" : <i>Double</i>,
        "<a href="#enablebotmansiem" title="EnableBotmanSiem">EnableBotmanSiem</a>" : <i>Boolean</i>,
        "<a href="#enableforallpolicies" title="EnableForAllPolicies">EnableForAllPolicies</a>" : <i>Boolean</i>,
        "<a href="#enablesiem" title="EnableSiem">EnableSiem</a>" : <i>Boolean</i>,
        "<a href="#securitypolicyids" title="SecurityPolicyIds">SecurityPolicyIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#siemid" title="SiemId">SiemId</a>" : <i>Double</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::AppsecSiemSettings
Properties:
    <a href="#configid" title="ConfigId">ConfigId</a>: <i>Double</i>
    <a href="#enablebotmansiem" title="EnableBotmanSiem">EnableBotmanSiem</a>: <i>Boolean</i>
    <a href="#enableforallpolicies" title="EnableForAllPolicies">EnableForAllPolicies</a>: <i>Boolean</i>
    <a href="#enablesiem" title="EnableSiem">EnableSiem</a>: <i>Boolean</i>
    <a href="#securitypolicyids" title="SecurityPolicyIds">SecurityPolicyIds</a>: <i>
      - String</i>
    <a href="#siemid" title="SiemId">SiemId</a>: <i>Double</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
</pre>

## Properties

#### ConfigId

The configuration ID to use.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableBotmanSiem

Whether you enabled SIEM for the Bot Manager events.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableForAllPolicies

Whether you enabled SIEM for all the security policies in the configuration version.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSiem

Whether you enabled SIEM in a security configuration version.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityPolicyIds

The list of security policy identifiers for which to enable the SIEM integration.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiemId

An integer that uniquely identifies the SIEM settings.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The version number of the configuration to use.

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

#### OutputText

Returns the <code>OutputText</code> value.

