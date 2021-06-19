# TF::FortiOS::EndpointcontrolProfile ForticlientIosSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clientvpnprovisioning" title="ClientVpnProvisioning">ClientVpnProvisioning</a>" : <i>String</i>,
    "<a href="#configurationcontent" title="ConfigurationContent">ConfigurationContent</a>" : <i>String</i>,
    "<a href="#configurationname" title="ConfigurationName">ConfigurationName</a>" : <i>String</i>,
    "<a href="#disablewfwhenprotected" title="DisableWfWhenProtected">DisableWfWhenProtected</a>" : <i>String</i>,
    "<a href="#distributeconfigurationprofile" title="DistributeConfigurationProfile">DistributeConfigurationProfile</a>" : <i>String</i>,
    "<a href="#forticlientwf" title="ForticlientWf">ForticlientWf</a>" : <i>String</i>,
    "<a href="#forticlientwfprofile" title="ForticlientWfProfile">ForticlientWfProfile</a>" : <i>String</i>,
    "<a href="#clientvpnsettings" title="ClientVpnSettings">ClientVpnSettings</a>" : <i>[ <a href="clientvpnsettingsdefinition.md">ClientVpnSettingsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clientvpnprovisioning" title="ClientVpnProvisioning">ClientVpnProvisioning</a>: <i>String</i>
<a href="#configurationcontent" title="ConfigurationContent">ConfigurationContent</a>: <i>String</i>
<a href="#configurationname" title="ConfigurationName">ConfigurationName</a>: <i>String</i>
<a href="#disablewfwhenprotected" title="DisableWfWhenProtected">DisableWfWhenProtected</a>: <i>String</i>
<a href="#distributeconfigurationprofile" title="DistributeConfigurationProfile">DistributeConfigurationProfile</a>: <i>String</i>
<a href="#forticlientwf" title="ForticlientWf">ForticlientWf</a>: <i>String</i>
<a href="#forticlientwfprofile" title="ForticlientWfProfile">ForticlientWfProfile</a>: <i>String</i>
<a href="#clientvpnsettings" title="ClientVpnSettings">ClientVpnSettings</a>: <i>
      - <a href="clientvpnsettingsdefinition.md">ClientVpnSettingsDefinition</a></i>
</pre>

## Properties

#### ClientVpnProvisioning

FortiClient VPN provisioning. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationContent

Content of configuration profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationName

Name of configuration profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableWfWhenProtected

Enable/disable FortiClient web category filtering when protected by FortiGate. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistributeConfigurationProfile

Enable/disable configuration profile (.mobileconfig file) distribution. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientWf

Enable/disable FortiClient web filtering. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientWfProfile

The FortiClient web filter profile to apply.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientVpnSettings

_Required_: No

_Type_: List of <a href="clientvpnsettingsdefinition.md">ClientVpnSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

