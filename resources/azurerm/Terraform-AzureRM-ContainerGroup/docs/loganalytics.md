# Terraform::AzureRM::ContainerGroup LogAnalytics

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#logtype" title="LogType">LogType</a>" : <i>String</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="loganalytics-metadata.md">Metadata</a>, ... ]</i>,
    "<a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>" : <i>String</i>,
    "<a href="#workspacekey" title="WorkspaceKey">WorkspaceKey</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#logtype" title="LogType">LogType</a>: <i>String</i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="loganalytics-metadata.md">Metadata</a></i>
<a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>: <i>String</i>
<a href="#workspacekey" title="WorkspaceKey">WorkspaceKey</a>: <i>String</i>
</pre>

## Properties

#### LogType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="loganalytics-metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

