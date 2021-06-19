# TF::AVI::Albservicesconfig

The ALBServicesConfig resource allows the creation and management of Avi ALBServicesConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Albservicesconfig",
    "Properties" : {
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#pollinginterval" title="PollingInterval">PollingInterval</a>" : <i>Double</i>,
        "<a href="#portalurl" title="PortalUrl">PortalUrl</a>" : <i>String</i>,
        "<a href="#usesplitproxy" title="UseSplitProxy">UseSplitProxy</a>" : <i>Boolean</i>,
        "<a href="#usetls" title="UseTls">UseTls</a>" : <i>Boolean</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#appsignatureconfig" title="AppSignatureConfig">AppSignatureConfig</a>" : <i>[ <a href="appsignatureconfigdefinition.md">AppSignatureConfigDefinition</a>, ... ]</i>,
        "<a href="#assetcontact" title="AssetContact">AssetContact</a>" : <i>[ <a href="assetcontactdefinition.md">AssetContactDefinition</a>, ... ]</i>,
        "<a href="#featureoptinstatus" title="FeatureOptInStatus">FeatureOptInStatus</a>" : <i>[ <a href="featureoptinstatusdefinition.md">FeatureOptInStatusDefinition</a>, ... ]</i>,
        "<a href="#ipreputationconfig" title="IpReputationConfig">IpReputationConfig</a>" : <i>[ <a href="ipreputationconfigdefinition.md">IpReputationConfigDefinition</a>, ... ]</i>,
        "<a href="#proactivesupportdefaults" title="ProactiveSupportDefaults">ProactiveSupportDefaults</a>" : <i>[ <a href="proactivesupportdefaultsdefinition.md">ProactiveSupportDefaultsDefinition</a>, ... ]</i>,
        "<a href="#splitproxyconfiguration" title="SplitProxyConfiguration">SplitProxyConfiguration</a>" : <i>[ <a href="splitproxyconfigurationdefinition.md">SplitProxyConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Albservicesconfig
Properties:
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#pollinginterval" title="PollingInterval">PollingInterval</a>: <i>Double</i>
    <a href="#portalurl" title="PortalUrl">PortalUrl</a>: <i>String</i>
    <a href="#usesplitproxy" title="UseSplitProxy">UseSplitProxy</a>: <i>Boolean</i>
    <a href="#usetls" title="UseTls">UseTls</a>: <i>Boolean</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#appsignatureconfig" title="AppSignatureConfig">AppSignatureConfig</a>: <i>
      - <a href="appsignatureconfigdefinition.md">AppSignatureConfigDefinition</a></i>
    <a href="#assetcontact" title="AssetContact">AssetContact</a>: <i>
      - <a href="assetcontactdefinition.md">AssetContactDefinition</a></i>
    <a href="#featureoptinstatus" title="FeatureOptInStatus">FeatureOptInStatus</a>: <i>
      - <a href="featureoptinstatusdefinition.md">FeatureOptInStatusDefinition</a></i>
    <a href="#ipreputationconfig" title="IpReputationConfig">IpReputationConfig</a>: <i>
      - <a href="ipreputationconfigdefinition.md">IpReputationConfigDefinition</a></i>
    <a href="#proactivesupportdefaults" title="ProactiveSupportDefaults">ProactiveSupportDefaults</a>: <i>
      - <a href="proactivesupportdefaultsdefinition.md">ProactiveSupportDefaultsDefinition</a></i>
    <a href="#splitproxyconfiguration" title="SplitProxyConfiguration">SplitProxyConfiguration</a>: <i>
      - <a href="splitproxyconfigurationdefinition.md">SplitProxyConfigurationDefinition</a></i>
</pre>

## Properties

#### Mode

Mode helps log collection and upload. Enum options - SALESFORCE, SYSTEST, MYVMWARE. Field introduced in 20.1.2. Allowed in basic(allowed values- salesforce,myvmware,systest) edition, essentials(allowed values- salesforce,myvmware,systest) edition, enterprise edition.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PollingInterval

Time interval in minutes. Allowed values are 5-60. Field introduced in 18.2.6.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortalUrl

The fqdn or ip address of the customer portal. Field introduced in 18.2.6.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseSplitProxy

By default, use system proxy configuration.if true, use split proxy configuration. Field introduced in 20.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseTls

Secure the controller to pulse communication over tls. Field introduced in 20.1.3. Allowed in basic edition, enterprise edition.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppSignatureConfig

_Required_: No

_Type_: List of <a href="appsignatureconfigdefinition.md">AppSignatureConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssetContact

_Required_: No

_Type_: List of <a href="assetcontactdefinition.md">AssetContactDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureOptInStatus

_Required_: No

_Type_: List of <a href="featureoptinstatusdefinition.md">FeatureOptInStatusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpReputationConfig

_Required_: No

_Type_: List of <a href="ipreputationconfigdefinition.md">IpReputationConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProactiveSupportDefaults

_Required_: No

_Type_: List of <a href="proactivesupportdefaultsdefinition.md">ProactiveSupportDefaultsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitProxyConfiguration

_Required_: No

_Type_: List of <a href="splitproxyconfigurationdefinition.md">SplitProxyConfigurationDefinition</a>

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

