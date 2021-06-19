# TF::AzureRM::MediaLiveEvent InputDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesstoken" title="AccessToken">AccessToken</a>" : <i>String</i>,
    "<a href="#keyframeintervalduration" title="KeyFrameIntervalDuration">KeyFrameIntervalDuration</a>" : <i>String</i>,
    "<a href="#streamingprotocol" title="StreamingProtocol">StreamingProtocol</a>" : <i>String</i>,
    "<a href="#ipaccesscontrolallow" title="IpAccessControlAllow">IpAccessControlAllow</a>" : <i>[ <a href="ipaccesscontrolallowdefinition.md">IpAccessControlAllowDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accesstoken" title="AccessToken">AccessToken</a>: <i>String</i>
<a href="#keyframeintervalduration" title="KeyFrameIntervalDuration">KeyFrameIntervalDuration</a>: <i>String</i>
<a href="#streamingprotocol" title="StreamingProtocol">StreamingProtocol</a>: <i>String</i>
<a href="#ipaccesscontrolallow" title="IpAccessControlAllow">IpAccessControlAllow</a>: <i>
      - <a href="ipaccesscontrolallowdefinition.md">IpAccessControlAllowDefinition</a></i>
</pre>

## Properties

#### AccessToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyFrameIntervalDuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamingProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAccessControlAllow

_Required_: No

_Type_: List of <a href="ipaccesscontrolallowdefinition.md">IpAccessControlAllowDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

