# TF::AzureRM::MediaLiveEvent PreviewDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alternativemediaid" title="AlternativeMediaId">AlternativeMediaId</a>" : <i>String</i>,
    "<a href="#previewlocator" title="PreviewLocator">PreviewLocator</a>" : <i>String</i>,
    "<a href="#streamingpolicyname" title="StreamingPolicyName">StreamingPolicyName</a>" : <i>String</i>,
    "<a href="#ipaccesscontrolallow" title="IpAccessControlAllow">IpAccessControlAllow</a>" : <i>[ <a href="ipaccesscontrolallowdefinition.md">IpAccessControlAllowDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alternativemediaid" title="AlternativeMediaId">AlternativeMediaId</a>: <i>String</i>
<a href="#previewlocator" title="PreviewLocator">PreviewLocator</a>: <i>String</i>
<a href="#streamingpolicyname" title="StreamingPolicyName">StreamingPolicyName</a>: <i>String</i>
<a href="#ipaccesscontrolallow" title="IpAccessControlAllow">IpAccessControlAllow</a>: <i>
      - <a href="ipaccesscontrolallowdefinition.md">IpAccessControlAllowDefinition</a></i>
</pre>

## Properties

#### AlternativeMediaId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreviewLocator

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamingPolicyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAccessControlAllow

_Required_: No

_Type_: List of <a href="ipaccesscontrolallowdefinition.md">IpAccessControlAllowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

