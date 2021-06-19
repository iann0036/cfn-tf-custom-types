# TF::CheckPoint::ManagementPackage

This resource allows you to add/update/delete Check Point Package Object.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementPackage",
    "Properties" : {
        "<a href="#access" title="Access">Access</a>" : <i>Boolean</i>,
        "<a href="#color" title="Color">Color</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#desktopsecurity" title="DesktopSecurity">DesktopSecurity</a>" : <i>Boolean</i>,
        "<a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>" : <i>Boolean</i>,
        "<a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>" : <i>Boolean</i>,
        "<a href="#installationtargets" title="InstallationTargets">InstallationTargets</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#qos" title="Qos">Qos</a>" : <i>Boolean</i>,
        "<a href="#qospolicytype" title="QosPolicyType">QosPolicyType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#threatprevention" title="ThreatPrevention">ThreatPrevention</a>" : <i>Boolean</i>,
        "<a href="#vpntraditionalmode" title="VpnTraditionalMode">VpnTraditionalMode</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementPackage
Properties:
    <a href="#access" title="Access">Access</a>: <i>Boolean</i>
    <a href="#color" title="Color">Color</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#desktopsecurity" title="DesktopSecurity">DesktopSecurity</a>: <i>Boolean</i>
    <a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>: <i>Boolean</i>
    <a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>: <i>Boolean</i>
    <a href="#installationtargets" title="InstallationTargets">InstallationTargets</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#qos" title="Qos">Qos</a>: <i>Boolean</i>
    <a href="#qospolicytype" title="QosPolicyType">QosPolicyType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#threatprevention" title="ThreatPrevention">ThreatPrevention</a>: <i>Boolean</i>
    <a href="#vpntraditionalmode" title="VpnTraditionalMode">VpnTraditionalMode</a>: <i>Boolean</i>
</pre>

## Properties

#### Access

True - enables, False - disables access & NAT policies, empty - nothing is changed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### DesktopSecurity

True - enables, False - disables Desktop security policy, empty - nothing is changed.

_Required_: No

_Type_: Boolean

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

#### InstallationTargets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Object name. Should be unique in the domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Qos

True - enables, False - disables QoS policy, empty - nothing is changed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QosPolicyType

QoS policy type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Collection of tag identifiers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatPrevention

True - enables, False - disables Threat policy, empty - nothing is changed.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpnTraditionalMode

True - enables, False - disables VPN traditional mode, empty - nothing is changed.

_Required_: No

_Type_: Boolean

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

