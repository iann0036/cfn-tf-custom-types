# Terraform::Google::FolderOrganizationPolicy

CloudFormation equivalent of google_folder_organization_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::FolderOrganizationPolicy",
    "Properties" : {
        "<a href="#constraint" title="Constraint">Constraint</a>" : <i>String</i>,
        "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>,
        "<a href="#booleanpolicy" title="BooleanPolicy">BooleanPolicy</a>" : <i>[ &lt;a href=&#34;booleanpolicy.md&#34;&gt;BooleanPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#listpolicy" title="ListPolicy">ListPolicy</a>" : <i>[ &lt;a href=&#34;listpolicy.md&#34;&gt;ListPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#restorepolicy" title="RestorePolicy">RestorePolicy</a>" : <i>[ &lt;a href=&#34;restorepolicy.md&#34;&gt;RestorePolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#allow" title="Allow">Allow</a>" : <i>[ &lt;a href=&#34;allow.md&#34;&gt;Allow&lt;/a&gt;, ... ]</i>,
        "<a href="#deny" title="Deny">Deny</a>" : <i>[ &lt;a href=&#34;deny.md&#34;&gt;Deny&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::FolderOrganizationPolicy
Properties:
    <a href="#constraint" title="Constraint">Constraint</a>: <i>String</i>
    <a href="#folder" title="Folder">Folder</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
    <a href="#booleanpolicy" title="BooleanPolicy">BooleanPolicy</a>: <i>
      - &lt;a href=&#34;booleanpolicy.md&#34;&gt;BooleanPolicy&lt;/a&gt;</i>
    <a href="#listpolicy" title="ListPolicy">ListPolicy</a>: <i>
      - &lt;a href=&#34;listpolicy.md&#34;&gt;ListPolicy&lt;/a&gt;</i>
    <a href="#restorepolicy" title="RestorePolicy">RestorePolicy</a>: <i>
      - &lt;a href=&#34;restorepolicy.md&#34;&gt;RestorePolicy&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#allow" title="Allow">Allow</a>: <i>
      - &lt;a href=&#34;allow.md&#34;&gt;Allow&lt;/a&gt;</i>
    <a href="#deny" title="Deny">Deny</a>: <i>
      - &lt;a href=&#34;deny.md&#34;&gt;Deny&lt;/a&gt;</i>
</pre>

## Properties

#### Constraint

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Folder

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BooleanPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;booleanpolicy.md&#34;&gt;BooleanPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ListPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;listpolicy.md&#34;&gt;ListPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestorePolicy

_Required_: No

_Type_: List of &lt;a href=&#34;restorepolicy.md&#34;&gt;RestorePolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Allow

_Required_: No

_Type_: List of &lt;a href=&#34;allow.md&#34;&gt;Allow&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deny

_Required_: No

_Type_: List of &lt;a href=&#34;deny.md&#34;&gt;Deny&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Etag

Returns the &lt;code&gt;Etag&lt;/code&gt; value.

#### UpdateTime

Returns the &lt;code&gt;UpdateTime&lt;/code&gt; value.

