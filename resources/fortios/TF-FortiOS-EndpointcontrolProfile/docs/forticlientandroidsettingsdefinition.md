# TF::FortiOS::EndpointcontrolProfile ForticlientAndroidSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disablewfwhenprotected" title="DisableWfWhenProtected">DisableWfWhenProtected</a>" : <i>String</i>,
    "<a href="#forticlientadvancedvpn" title="ForticlientAdvancedVpn">ForticlientAdvancedVpn</a>" : <i>String</i>,
    "<a href="#forticlientadvancedvpnbuffer" title="ForticlientAdvancedVpnBuffer">ForticlientAdvancedVpnBuffer</a>" : <i>String</i>,
    "<a href="#forticlientvpnprovisioning" title="ForticlientVpnProvisioning">ForticlientVpnProvisioning</a>" : <i>String</i>,
    "<a href="#forticlientwf" title="ForticlientWf">ForticlientWf</a>" : <i>String</i>,
    "<a href="#forticlientwfprofile" title="ForticlientWfProfile">ForticlientWfProfile</a>" : <i>String</i>,
    "<a href="#forticlientvpnsettings" title="ForticlientVpnSettings">ForticlientVpnSettings</a>" : <i>[ <a href="forticlientvpnsettingsdefinition.md">ForticlientVpnSettingsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disablewfwhenprotected" title="DisableWfWhenProtected">DisableWfWhenProtected</a>: <i>String</i>
<a href="#forticlientadvancedvpn" title="ForticlientAdvancedVpn">ForticlientAdvancedVpn</a>: <i>String</i>
<a href="#forticlientadvancedvpnbuffer" title="ForticlientAdvancedVpnBuffer">ForticlientAdvancedVpnBuffer</a>: <i>String</i>
<a href="#forticlientvpnprovisioning" title="ForticlientVpnProvisioning">ForticlientVpnProvisioning</a>: <i>String</i>
<a href="#forticlientwf" title="ForticlientWf">ForticlientWf</a>: <i>String</i>
<a href="#forticlientwfprofile" title="ForticlientWfProfile">ForticlientWfProfile</a>: <i>String</i>
<a href="#forticlientvpnsettings" title="ForticlientVpnSettings">ForticlientVpnSettings</a>: <i>
      - <a href="forticlientvpnsettingsdefinition.md">ForticlientVpnSettingsDefinition</a></i>
</pre>

## Properties

#### DisableWfWhenProtected

Enable/disable FortiClient web category filtering when protected by FortiGate. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientAdvancedVpn

Enable/disable advanced FortiClient VPN configuration. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientAdvancedVpnBuffer

Advanced FortiClient VPN configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientVpnProvisioning

Enable/disable FortiClient VPN provisioning. Valid values: `enable`, `disable`.

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

#### ForticlientVpnSettings

_Required_: No

_Type_: List of <a href="forticlientvpnsettingsdefinition.md">ForticlientVpnSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

