# Terraform::GitHub::Repository

CloudFormation equivalent of github_repository

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::GitHub::Repository",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#allowmergecommit" title="AllowMergeCommit">AllowMergeCommit</a>" : <i>Boolean</i>,
        "<a href="#allowrebasemerge" title="AllowRebaseMerge">AllowRebaseMerge</a>" : <i>Boolean</i>,
        "<a href="#allowsquashmerge" title="AllowSquashMerge">AllowSquashMerge</a>" : <i>Boolean</i>,
        "<a href="#archived" title="Archived">Archived</a>" : <i>Boolean</i>,
        "<a href="#autoinit" title="AutoInit">AutoInit</a>" : <i>Boolean</i>,
        "<a href="#defaultbranch" title="DefaultBranch">DefaultBranch</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#etag" title="Etag">Etag</a>" : <i>String</i>,
        "<a href="#fullname" title="FullName">FullName</a>" : <i>String</i>,
        "<a href="#gitcloneurl" title="GitCloneUrl">GitCloneUrl</a>" : <i>String</i>,
        "<a href="#gitignoretemplate" title="GitignoreTemplate">GitignoreTemplate</a>" : <i>String</i>,
        "<a href="#hasdownloads" title="HasDownloads">HasDownloads</a>" : <i>Boolean</i>,
        "<a href="#hasissues" title="HasIssues">HasIssues</a>" : <i>Boolean</i>,
        "<a href="#hasprojects" title="HasProjects">HasProjects</a>" : <i>Boolean</i>,
        "<a href="#haswiki" title="HasWiki">HasWiki</a>" : <i>Boolean</i>,
        "<a href="#homepageurl" title="HomepageUrl">HomepageUrl</a>" : <i>String</i>,
        "<a href="#htmlurl" title="HtmlUrl">HtmlUrl</a>" : <i>String</i>,
        "<a href="#httpcloneurl" title="HttpCloneUrl">HttpCloneUrl</a>" : <i>String</i>,
        "<a href="#licensetemplate" title="LicenseTemplate">LicenseTemplate</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#private" title="Private">Private</a>" : <i>Boolean</i>,
        "<a href="#sshcloneurl" title="SshCloneUrl">SshCloneUrl</a>" : <i>String</i>,
        "<a href="#svnurl" title="SvnUrl">SvnUrl</a>" : <i>String</i>,
        "<a href="#topics" title="Topics">Topics</a>" : <i>[ String, ... ]</i>,
        "<a href="#template" title="Template">Template</a>" : <i>[ &lt;a href=&#34;template.md&#34;&gt;Template&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::GitHub::Repository
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#allowmergecommit" title="AllowMergeCommit">AllowMergeCommit</a>: <i>Boolean</i>
    <a href="#allowrebasemerge" title="AllowRebaseMerge">AllowRebaseMerge</a>: <i>Boolean</i>
    <a href="#allowsquashmerge" title="AllowSquashMerge">AllowSquashMerge</a>: <i>Boolean</i>
    <a href="#archived" title="Archived">Archived</a>: <i>Boolean</i>
    <a href="#autoinit" title="AutoInit">AutoInit</a>: <i>Boolean</i>
    <a href="#defaultbranch" title="DefaultBranch">DefaultBranch</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#etag" title="Etag">Etag</a>: <i>String</i>
    <a href="#fullname" title="FullName">FullName</a>: <i>String</i>
    <a href="#gitcloneurl" title="GitCloneUrl">GitCloneUrl</a>: <i>String</i>
    <a href="#gitignoretemplate" title="GitignoreTemplate">GitignoreTemplate</a>: <i>String</i>
    <a href="#hasdownloads" title="HasDownloads">HasDownloads</a>: <i>Boolean</i>
    <a href="#hasissues" title="HasIssues">HasIssues</a>: <i>Boolean</i>
    <a href="#hasprojects" title="HasProjects">HasProjects</a>: <i>Boolean</i>
    <a href="#haswiki" title="HasWiki">HasWiki</a>: <i>Boolean</i>
    <a href="#homepageurl" title="HomepageUrl">HomepageUrl</a>: <i>String</i>
    <a href="#htmlurl" title="HtmlUrl">HtmlUrl</a>: <i>String</i>
    <a href="#httpcloneurl" title="HttpCloneUrl">HttpCloneUrl</a>: <i>String</i>
    <a href="#licensetemplate" title="LicenseTemplate">LicenseTemplate</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#private" title="Private">Private</a>: <i>Boolean</i>
    <a href="#sshcloneurl" title="SshCloneUrl">SshCloneUrl</a>: <i>String</i>
    <a href="#svnurl" title="SvnUrl">SvnUrl</a>: <i>String</i>
    <a href="#topics" title="Topics">Topics</a>: <i>
      - String</i>
    <a href="#template" title="Template">Template</a>: <i>
      - &lt;a href=&#34;template.md&#34;&gt;Template&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowMergeCommit

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowRebaseMerge

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowSquashMerge

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Archived

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoInit

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultBranch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Etag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitCloneUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitignoreTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasDownloads

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasIssues

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasProjects

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasWiki

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HomepageUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HtmlUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpCloneUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Private

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshCloneUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SvnUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Topics

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: List of &lt;a href=&#34;template.md&#34;&gt;Template&lt;/a&gt;

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

#### FullName

Returns the &lt;code&gt;FullName&lt;/code&gt; value.

#### GitCloneUrl

Returns the &lt;code&gt;GitCloneUrl&lt;/code&gt; value.

#### HtmlUrl

Returns the &lt;code&gt;HtmlUrl&lt;/code&gt; value.

#### HttpCloneUrl

Returns the &lt;code&gt;HttpCloneUrl&lt;/code&gt; value.

#### SshCloneUrl

Returns the &lt;code&gt;SshCloneUrl&lt;/code&gt; value.

#### SvnUrl

Returns the &lt;code&gt;SvnUrl&lt;/code&gt; value.

