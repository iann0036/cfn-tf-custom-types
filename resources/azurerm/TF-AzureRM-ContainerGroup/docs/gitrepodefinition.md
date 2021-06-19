# TF::AzureRM::ContainerGroup GitRepoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#directory" title="Directory">Directory</a>" : <i>String</i>,
    "<a href="#revision" title="Revision">Revision</a>" : <i>String</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#directory" title="Directory">Directory</a>: <i>String</i>
<a href="#revision" title="Revision">Revision</a>: <i>String</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
</pre>

## Properties

#### Directory

Specifies the directory into which the repository should be cloned. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Revision

Specifies the commit hash of the revision to be cloned. If unspecified, the HEAD revision is cloned. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

Specifies the Git repository to be cloned. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

