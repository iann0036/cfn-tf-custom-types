# TF::Artifactory::XrayPolicy ActionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customseverity" title="CustomSeverity">CustomSeverity</a>" : <i>String</i>,
    "<a href="#failbuild" title="FailBuild">FailBuild</a>" : <i>Boolean</i>,
    "<a href="#mails" title="Mails">Mails</a>" : <i>[ String, ... ]</i>,
    "<a href="#webhooks" title="Webhooks">Webhooks</a>" : <i>[ String, ... ]</i>,
    "<a href="#blockdownload" title="BlockDownload">BlockDownload</a>" : <i>[ <a href="blockdownloaddefinition.md">BlockDownloadDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#customseverity" title="CustomSeverity">CustomSeverity</a>: <i>String</i>
<a href="#failbuild" title="FailBuild">FailBuild</a>: <i>Boolean</i>
<a href="#mails" title="Mails">Mails</a>: <i>
      - String</i>
<a href="#webhooks" title="Webhooks">Webhooks</a>: <i>
      - String</i>
<a href="#blockdownload" title="BlockDownload">BlockDownload</a>: <i>
      - <a href="blockdownloaddefinition.md">BlockDownloadDefinition</a></i>
</pre>

## Properties

#### CustomSeverity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailBuild

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mails

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webhooks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockDownload

_Required_: No

_Type_: List of <a href="blockdownloaddefinition.md">BlockDownloadDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

