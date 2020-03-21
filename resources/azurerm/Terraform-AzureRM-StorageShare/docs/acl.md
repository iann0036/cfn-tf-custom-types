# Terraform::AzureRM::StorageShare Acl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#accesspolicy" title="AccessPolicy">AccessPolicy</a>" : <i>[ &lt;a href=&#34;acl-accesspolicy.md&#34;&gt;AccessPolicy&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#accesspolicy" title="AccessPolicy">AccessPolicy</a>: <i>
      - &lt;a href=&#34;acl-accesspolicy.md&#34;&gt;AccessPolicy&lt;/a&gt;</i>
</pre>

## Properties

#### Id

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessPolicy

_Required_: No
_Type_: List of &lt;a href=&#34;acl-accesspolicy.md&#34;&gt;AccessPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

