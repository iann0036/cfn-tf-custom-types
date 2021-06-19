# TF::CheckPoint::ManagementThreatProfile

This resource allows you to add/update/delete Check Point Threat Profile.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementThreatProfile",
    "Properties" : {
        "<a href="#activeprotectionsperformanceimpact" title="ActiveProtectionsPerformanceImpact">ActiveProtectionsPerformanceImpact</a>" : <i>String</i>,
        "<a href="#activeprotectionsseverity" title="ActiveProtectionsSeverity">ActiveProtectionsSeverity</a>" : <i>String</i>,
        "<a href="#antibot" title="AntiBot">AntiBot</a>" : <i>Boolean</i>,
        "<a href="#antivirus" title="AntiVirus">AntiVirus</a>" : <i>Boolean</i>,
        "<a href="#color" title="Color">Color</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#confidencelevelhigh" title="ConfidenceLevelHigh">ConfidenceLevelHigh</a>" : <i>String</i>,
        "<a href="#confidencelevellow" title="ConfidenceLevelLow">ConfidenceLevelLow</a>" : <i>String</i>,
        "<a href="#confidencelevelmedium" title="ConfidenceLevelMedium">ConfidenceLevelMedium</a>" : <i>String</i>,
        "<a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>" : <i>Boolean</i>,
        "<a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>" : <i>Boolean</i>,
        "<a href="#ips" title="Ips">Ips</a>" : <i>Boolean</i>,
        "<a href="#ipssettings" title="IpsSettings">IpsSettings</a>" : <i>[ <a href="ipssettingsdefinition.md">IpsSettingsDefinition</a>, ... ]</i>,
        "<a href="#maliciousmailpolicysettings" title="MaliciousMailPolicySettings">MaliciousMailPolicySettings</a>" : <i>[ <a href="maliciousmailpolicysettingsdefinition.md">MaliciousMailPolicySettingsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#scanmaliciouslinks" title="ScanMaliciousLinks">ScanMaliciousLinks</a>" : <i>[ <a href="scanmaliciouslinksdefinition.md">ScanMaliciousLinksDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#threatemulation" title="ThreatEmulation">ThreatEmulation</a>" : <i>Boolean</i>,
        "<a href="#useextendedattributes" title="UseExtendedAttributes">UseExtendedAttributes</a>" : <i>Boolean</i>,
        "<a href="#useindicators" title="UseIndicators">UseIndicators</a>" : <i>Boolean</i>,
        "<a href="#deactivateprotectionsbyextendedattributes" title="DeactivateProtectionsByExtendedAttributes">DeactivateProtectionsByExtendedAttributes</a>" : <i>[ <a href="deactivateprotectionsbyextendedattributesdefinition.md">DeactivateProtectionsByExtendedAttributesDefinition</a>, ... ]</i>,
        "<a href="#indicatoroverrides" title="IndicatorOverrides">IndicatorOverrides</a>" : <i>[ <a href="indicatoroverridesdefinition.md">IndicatorOverridesDefinition</a>, ... ]</i>,
        "<a href="#overrides" title="Overrides">Overrides</a>" : <i>[ <a href="overridesdefinition.md">OverridesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementThreatProfile
Properties:
    <a href="#activeprotectionsperformanceimpact" title="ActiveProtectionsPerformanceImpact">ActiveProtectionsPerformanceImpact</a>: <i>String</i>
    <a href="#activeprotectionsseverity" title="ActiveProtectionsSeverity">ActiveProtectionsSeverity</a>: <i>String</i>
    <a href="#antibot" title="AntiBot">AntiBot</a>: <i>Boolean</i>
    <a href="#antivirus" title="AntiVirus">AntiVirus</a>: <i>Boolean</i>
    <a href="#color" title="Color">Color</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#confidencelevelhigh" title="ConfidenceLevelHigh">ConfidenceLevelHigh</a>: <i>String</i>
    <a href="#confidencelevellow" title="ConfidenceLevelLow">ConfidenceLevelLow</a>: <i>String</i>
    <a href="#confidencelevelmedium" title="ConfidenceLevelMedium">ConfidenceLevelMedium</a>: <i>String</i>
    <a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>: <i>Boolean</i>
    <a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>: <i>Boolean</i>
    <a href="#ips" title="Ips">Ips</a>: <i>Boolean</i>
    <a href="#ipssettings" title="IpsSettings">IpsSettings</a>: <i>
      - <a href="ipssettingsdefinition.md">IpsSettingsDefinition</a></i>
    <a href="#maliciousmailpolicysettings" title="MaliciousMailPolicySettings">MaliciousMailPolicySettings</a>: <i>
      - <a href="maliciousmailpolicysettingsdefinition.md">MaliciousMailPolicySettingsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#scanmaliciouslinks" title="ScanMaliciousLinks">ScanMaliciousLinks</a>: <i>
      - <a href="scanmaliciouslinksdefinition.md">ScanMaliciousLinksDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#threatemulation" title="ThreatEmulation">ThreatEmulation</a>: <i>Boolean</i>
    <a href="#useextendedattributes" title="UseExtendedAttributes">UseExtendedAttributes</a>: <i>Boolean</i>
    <a href="#useindicators" title="UseIndicators">UseIndicators</a>: <i>Boolean</i>
    <a href="#deactivateprotectionsbyextendedattributes" title="DeactivateProtectionsByExtendedAttributes">DeactivateProtectionsByExtendedAttributes</a>: <i>
      - <a href="deactivateprotectionsbyextendedattributesdefinition.md">DeactivateProtectionsByExtendedAttributesDefinition</a></i>
    <a href="#indicatoroverrides" title="IndicatorOverrides">IndicatorOverrides</a>: <i>
      - <a href="indicatoroverridesdefinition.md">IndicatorOverridesDefinition</a></i>
    <a href="#overrides" title="Overrides">Overrides</a>: <i>
      - <a href="overridesdefinition.md">OverridesDefinition</a></i>
</pre>

## Properties

#### ActiveProtectionsPerformanceImpact

Protections with this performance impact only will be activated in the profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActiveProtectionsSeverity

Protections with this severity only will be activated in the profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntiBot

Is Anti-Bot blade activated.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AntiVirus

Is Anti-Virus blade activated.

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

#### ConfidenceLevelHigh

Action for protections with high confidence level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfidenceLevelLow

Action for protections with low confidence level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfidenceLevelMedium

Action for protections with medium confidence level.

_Required_: No

_Type_: String

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

#### Ips

Is IPS blade activated.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsSettings

IPS blade settings. ips_settings blocks are documented below.

_Required_: No

_Type_: List of <a href="ipssettingsdefinition.md">IpsSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaliciousMailPolicySettings

Malicious Mail Policy for MTA Gateways. malicious_mail_policy_settings blocks are documented below.

_Required_: No

_Type_: List of <a href="maliciousmailpolicysettingsdefinition.md">MaliciousMailPolicySettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Object name. Should be unique in the domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScanMaliciousLinks

Scans malicious links (URLs) inside email messages. scan_malicious_links blocks are documented below.

_Required_: No

_Type_: List of <a href="scanmaliciouslinksdefinition.md">ScanMaliciousLinksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Collection of tag identifiers.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatEmulation

Is Threat Emulation blade activated.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseExtendedAttributes

Whether to activate/deactivate IPS protections according to the extended attributes.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseIndicators

Indicates whether the profile should make use of indicators.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeactivateProtectionsByExtendedAttributes

_Required_: No

_Type_: List of <a href="deactivateprotectionsbyextendedattributesdefinition.md">DeactivateProtectionsByExtendedAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IndicatorOverrides

_Required_: No

_Type_: List of <a href="indicatoroverridesdefinition.md">IndicatorOverridesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overrides

_Required_: No

_Type_: List of <a href="overridesdefinition.md">OverridesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ActivateProtectionsByExtendedAttributes

Activate protections by these extended attributes. activate_protections_by_extended_attributes blocks are documented below.

#### Id

Returns the <code>Id</code> value.

