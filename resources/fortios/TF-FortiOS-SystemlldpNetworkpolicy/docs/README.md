# TF::FortiOS::SystemlldpNetworkpolicy

Configure LLDP network policy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemlldpNetworkpolicy",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#guest" title="Guest">Guest</a>" : <i>[ <a href="guestdefinition.md">GuestDefinition</a>, ... ]</i>,
        "<a href="#guestvoicesignaling" title="GuestVoiceSignaling">GuestVoiceSignaling</a>" : <i>[ <a href="guestvoicesignalingdefinition.md">GuestVoiceSignalingDefinition</a>, ... ]</i>,
        "<a href="#softphone" title="Softphone">Softphone</a>" : <i>[ <a href="softphonedefinition.md">SoftphoneDefinition</a>, ... ]</i>,
        "<a href="#streamingvideo" title="StreamingVideo">StreamingVideo</a>" : <i>[ <a href="streamingvideodefinition.md">StreamingVideoDefinition</a>, ... ]</i>,
        "<a href="#videoconferencing" title="VideoConferencing">VideoConferencing</a>" : <i>[ <a href="videoconferencingdefinition.md">VideoConferencingDefinition</a>, ... ]</i>,
        "<a href="#videosignaling" title="VideoSignaling">VideoSignaling</a>" : <i>[ <a href="videosignalingdefinition.md">VideoSignalingDefinition</a>, ... ]</i>,
        "<a href="#voice" title="Voice">Voice</a>" : <i>[ <a href="voicedefinition.md">VoiceDefinition</a>, ... ]</i>,
        "<a href="#voicesignaling" title="VoiceSignaling">VoiceSignaling</a>" : <i>[ <a href="voicesignalingdefinition.md">VoiceSignalingDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemlldpNetworkpolicy
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#guest" title="Guest">Guest</a>: <i>
      - <a href="guestdefinition.md">GuestDefinition</a></i>
    <a href="#guestvoicesignaling" title="GuestVoiceSignaling">GuestVoiceSignaling</a>: <i>
      - <a href="guestvoicesignalingdefinition.md">GuestVoiceSignalingDefinition</a></i>
    <a href="#softphone" title="Softphone">Softphone</a>: <i>
      - <a href="softphonedefinition.md">SoftphoneDefinition</a></i>
    <a href="#streamingvideo" title="StreamingVideo">StreamingVideo</a>: <i>
      - <a href="streamingvideodefinition.md">StreamingVideoDefinition</a></i>
    <a href="#videoconferencing" title="VideoConferencing">VideoConferencing</a>: <i>
      - <a href="videoconferencingdefinition.md">VideoConferencingDefinition</a></i>
    <a href="#videosignaling" title="VideoSignaling">VideoSignaling</a>: <i>
      - <a href="videosignalingdefinition.md">VideoSignalingDefinition</a></i>
    <a href="#voice" title="Voice">Voice</a>: <i>
      - <a href="voicedefinition.md">VoiceDefinition</a></i>
    <a href="#voicesignaling" title="VoiceSignaling">VoiceSignaling</a>: <i>
      - <a href="voicesignalingdefinition.md">VoiceSignalingDefinition</a></i>
</pre>

## Properties

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

LLDP network policy name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Guest

_Required_: No

_Type_: List of <a href="guestdefinition.md">GuestDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuestVoiceSignaling

_Required_: No

_Type_: List of <a href="guestvoicesignalingdefinition.md">GuestVoiceSignalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Softphone

_Required_: No

_Type_: List of <a href="softphonedefinition.md">SoftphoneDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamingVideo

_Required_: No

_Type_: List of <a href="streamingvideodefinition.md">StreamingVideoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VideoConferencing

_Required_: No

_Type_: List of <a href="videoconferencingdefinition.md">VideoConferencingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VideoSignaling

_Required_: No

_Type_: List of <a href="videosignalingdefinition.md">VideoSignalingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Voice

_Required_: No

_Type_: List of <a href="voicedefinition.md">VoiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VoiceSignaling

_Required_: No

_Type_: List of <a href="voicesignalingdefinition.md">VoiceSignalingDefinition</a>

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

