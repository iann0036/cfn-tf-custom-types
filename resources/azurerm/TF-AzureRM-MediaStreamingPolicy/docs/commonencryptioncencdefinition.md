# TF::AzureRM::MediaStreamingPolicy CommonEncryptionCencDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#drmwidevinecustomlicenseacquisitionurltemplate" title="DrmWidevineCustomLicenseAcquisitionUrlTemplate">DrmWidevineCustomLicenseAcquisitionUrlTemplate</a>" : <i>String</i>,
    "<a href="#defaultcontentkey" title="DefaultContentKey">DefaultContentKey</a>" : <i>[ <a href="defaultcontentkeydefinition.md">DefaultContentKeyDefinition</a>, ... ]</i>,
    "<a href="#drmplayready" title="DrmPlayready">DrmPlayready</a>" : <i>[ <a href="drmplayreadydefinition.md">DrmPlayreadyDefinition</a>, ... ]</i>,
    "<a href="#enabledprotocols" title="EnabledProtocols">EnabledProtocols</a>" : <i>[ <a href="enabledprotocolsdefinition.md">EnabledProtocolsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#drmwidevinecustomlicenseacquisitionurltemplate" title="DrmWidevineCustomLicenseAcquisitionUrlTemplate">DrmWidevineCustomLicenseAcquisitionUrlTemplate</a>: <i>String</i>
<a href="#defaultcontentkey" title="DefaultContentKey">DefaultContentKey</a>: <i>
      - <a href="defaultcontentkeydefinition.md">DefaultContentKeyDefinition</a></i>
<a href="#drmplayready" title="DrmPlayready">DrmPlayready</a>: <i>
      - <a href="drmplayreadydefinition.md">DrmPlayreadyDefinition</a></i>
<a href="#enabledprotocols" title="EnabledProtocols">EnabledProtocols</a>: <i>
      - <a href="enabledprotocolsdefinition.md">EnabledProtocolsDefinition</a></i>
</pre>

## Properties

#### DrmWidevineCustomLicenseAcquisitionUrlTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultContentKey

_Required_: No

_Type_: List of <a href="defaultcontentkeydefinition.md">DefaultContentKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrmPlayready

_Required_: No

_Type_: List of <a href="drmplayreadydefinition.md">DrmPlayreadyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnabledProtocols

_Required_: No

_Type_: List of <a href="enabledprotocolsdefinition.md">EnabledProtocolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

