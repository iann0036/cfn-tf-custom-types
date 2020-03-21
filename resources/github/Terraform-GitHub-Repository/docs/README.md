# Terraform::GitHub::Repository

CloudFormation equivalent of github_repository

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::GitHub::Repository",
    "Properties" : {
        "<a href="#allowmergecommit" title="AllowMergeCommit">AllowMergeCommit</a>" : <i>Boolean</i>,
        "<a href="#allowrebasemerge" title="AllowRebaseMerge">AllowRebaseMerge</a>" : <i>Boolean</i>,
        "<a href="#allowsquashmerge" title="AllowSquashMerge">AllowSquashMerge</a>" : <i>Boolean</i>,
        "<a href="#archived" title="Archived">Archived</a>" : <i>Boolean</i>,
        "<a href="#autoinit" title="AutoInit">AutoInit</a>" : <i>Boolean</i>,
        "<a href="#defaultbranch" title="DefaultBranch">DefaultBranch</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#gitignoretemplate" title="GitignoreTemplate">GitignoreTemplate</a>" : <i>String</i>,
        "<a href="#hasdownloads" title="HasDownloads">HasDownloads</a>" : <i>Boolean</i>,
        "<a href="#hasissues" title="HasIssues">HasIssues</a>" : <i>Boolean</i>,
        "<a href="#hasprojects" title="HasProjects">HasProjects</a>" : <i>Boolean</i>,
        "<a href="#haswiki" title="HasWiki">HasWiki</a>" : <i>Boolean</i>,
        "<a href="#homepageurl" title="HomepageUrl">HomepageUrl</a>" : <i>String</i>,
        "<a href="#licensetemplate" title="LicenseTemplate">LicenseTemplate</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#private" title="Private">Private</a>" : <i>Boolean</i>,
        "<a href="#topics" title="Topics">Topics</a>" : <i>[ String, ... ]</i>,
        "<a href="#template" title="Template">Template</a>" : <i>[ <a href="template.md">Template</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::GitHub::Repository
Properties:
    <a href="#allowmergecommit" title="AllowMergeCommit">AllowMergeCommit</a>: <i>Boolean</i>
    <a href="#allowrebasemerge" title="AllowRebaseMerge">AllowRebaseMerge</a>: <i>Boolean</i>
    <a href="#allowsquashmerge" title="AllowSquashMerge">AllowSquashMerge</a>: <i>Boolean</i>
    <a href="#archived" title="Archived">Archived</a>: <i>Boolean</i>
    <a href="#autoinit" title="AutoInit">AutoInit</a>: <i>Boolean</i>
    <a href="#defaultbranch" title="DefaultBranch">DefaultBranch</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#gitignoretemplate" title="GitignoreTemplate">GitignoreTemplate</a>: <i>String</i>
    <a href="#hasdownloads" title="HasDownloads">HasDownloads</a>: <i>Boolean</i>
    <a href="#hasissues" title="HasIssues">HasIssues</a>: <i>Boolean</i>
    <a href="#hasprojects" title="HasProjects">HasProjects</a>: <i>Boolean</i>
    <a href="#haswiki" title="HasWiki">HasWiki</a>: <i>Boolean</i>
    <a href="#homepageurl" title="HomepageUrl">HomepageUrl</a>: <i>String</i>
    <a href="#licensetemplate" title="LicenseTemplate">LicenseTemplate</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#private" title="Private">Private</a>: <i>Boolean</i>
    <a href="#topics" title="Topics">Topics</a>: <i>
      - String</i>
    <a href="#template" title="Template">Template</a>: <i>
      - <a href="template.md">Template</a></i>
</pre>

## Properties

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

#### Topics

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: List of <a href="template.md">Template</a>

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

Returns the <code>Etag</code> value.

#### FullName

Returns the <code>FullName</code> value.

#### GitCloneUrl

Returns the <code>GitCloneUrl</code> value.

#### HtmlUrl

Returns the <code>HtmlUrl</code> value.

#### HttpCloneUrl

Returns the <code>HttpCloneUrl</code> value.

#### SshCloneUrl

Returns the <code>SshCloneUrl</code> value.

#### SvnUrl

Returns the <code>SvnUrl</code> value.

