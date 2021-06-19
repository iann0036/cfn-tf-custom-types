# TF::Cloudflare::CustomHostname SslDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificateauthority" title="CertificateAuthority">CertificateAuthority</a>" : <i>String</i>,
    "<a href="#cnamename" title="CnameName">CnameName</a>" : <i>String</i>,
    "<a href="#cnametarget" title="CnameTarget">CnameTarget</a>" : <i>String</i>,
    "<a href="#customcertificate" title="CustomCertificate">CustomCertificate</a>" : <i>String</i>,
    "<a href="#customkey" title="CustomKey">CustomKey</a>" : <i>String</i>,
    "<a href="#method" title="Method">Method</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#wildcard" title="Wildcard">Wildcard</a>" : <i>Boolean</i>,
    "<a href="#settings" title="Settings">Settings</a>" : <i>[ <a href="settingsdefinition.md">SettingsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#certificateauthority" title="CertificateAuthority">CertificateAuthority</a>: <i>String</i>
<a href="#cnamename" title="CnameName">CnameName</a>: <i>String</i>
<a href="#cnametarget" title="CnameTarget">CnameTarget</a>: <i>String</i>
<a href="#customcertificate" title="CustomCertificate">CustomCertificate</a>: <i>String</i>
<a href="#customkey" title="CustomKey">CustomKey</a>: <i>String</i>
<a href="#method" title="Method">Method</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#wildcard" title="Wildcard">Wildcard</a>: <i>Boolean</i>
<a href="#settings" title="Settings">Settings</a>: <i>
      - <a href="settingsdefinition.md">SettingsDefinition</a></i>
</pre>

## Properties

#### CertificateAuthority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CnameName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CnameTarget

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomCertificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wildcard

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Settings

_Required_: No

_Type_: List of <a href="settingsdefinition.md">SettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

