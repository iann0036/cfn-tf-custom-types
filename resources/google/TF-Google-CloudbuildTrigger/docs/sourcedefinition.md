# TF::Google::CloudbuildTrigger SourceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#reposource" title="RepoSource">RepoSource</a>" : <i>[ <a href="reposourcedefinition.md">RepoSourceDefinition</a>, ... ]</i>,
    "<a href="#storagesource" title="StorageSource">StorageSource</a>" : <i>[ <a href="storagesourcedefinition.md">StorageSourceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#reposource" title="RepoSource">RepoSource</a>: <i>
      - <a href="reposourcedefinition.md">RepoSourceDefinition</a></i>
<a href="#storagesource" title="StorageSource">StorageSource</a>: <i>
      - <a href="storagesourcedefinition.md">StorageSourceDefinition</a></i>
</pre>

## Properties

#### RepoSource

_Required_: No

_Type_: List of <a href="reposourcedefinition.md">RepoSourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageSource

_Required_: No

_Type_: List of <a href="storagesourcedefinition.md">StorageSourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

