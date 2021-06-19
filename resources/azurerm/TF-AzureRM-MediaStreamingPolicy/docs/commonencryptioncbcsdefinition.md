# TF::AzureRM::MediaStreamingPolicy CommonEncryptionCbcsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultcontentkey" title="DefaultContentKey">DefaultContentKey</a>" : <i>[ <a href="defaultcontentkeydefinition.md">DefaultContentKeyDefinition</a>, ... ]</i>,
    "<a href="#drmfairplay" title="DrmFairplay">DrmFairplay</a>" : <i>[ <a href="drmfairplaydefinition.md">DrmFairplayDefinition</a>, ... ]</i>,
    "<a href="#enabledprotocols" title="EnabledProtocols">EnabledProtocols</a>" : <i>[ <a href="enabledprotocolsdefinition.md">EnabledProtocolsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultcontentkey" title="DefaultContentKey">DefaultContentKey</a>: <i>
      - <a href="defaultcontentkeydefinition.md">DefaultContentKeyDefinition</a></i>
<a href="#drmfairplay" title="DrmFairplay">DrmFairplay</a>: <i>
      - <a href="drmfairplaydefinition.md">DrmFairplayDefinition</a></i>
<a href="#enabledprotocols" title="EnabledProtocols">EnabledProtocols</a>: <i>
      - <a href="enabledprotocolsdefinition.md">EnabledProtocolsDefinition</a></i>
</pre>

## Properties

#### DefaultContentKey

_Required_: No

_Type_: List of <a href="defaultcontentkeydefinition.md">DefaultContentKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrmFairplay

_Required_: No

_Type_: List of <a href="drmfairplaydefinition.md">DrmFairplayDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnabledProtocols

_Required_: No

_Type_: List of <a href="enabledprotocolsdefinition.md">EnabledProtocolsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

