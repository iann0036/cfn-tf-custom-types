# Terraform::GitHub::Repository

This resource allows you to create and manage repositories within your
GitHub organization.

This resource cannot currently be used to manage *personal* repositories,
outside of organizations.

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

Set to `false` to disable merge commits on the repository.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowRebaseMerge

Set to `false` to disable rebase merges on the repository.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowSquashMerge

Set to `false` to disable squash merges on the repository.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Archived

Specifies if the repository should be archived. Defaults to `false`. **NOTE** Currently, the API does not support unarchiving.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoInit

Set to `true` to produce an initial commit in the repository.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultBranch

The name of the default branch of the repository. **NOTE:** This can only be set after a repository has already been created,
and after a correct reference has been created for the target branch inside the repository. This means a user will have to omit this parameter from the
initial repository creation and create the target branch inside of the repository prior to setting this attribute.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the repository.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitignoreTemplate

Use the [name of the template](https://github.com/github/gitignore) without the extension. For example, "Haskell".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasDownloads

Set to `true` to enable the (deprecated) downloads features on the repository.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasIssues

Set to `true` to enable the GitHub Issues features
on the repository.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasProjects

Set to `true` to enable the GitHub Projects features on the repository. Per the GitHub [documentation](https://developer.github.com/v3/repos/#create) when in an organization that has disabled repository projects it will default to `false` and will otherwise default to `true`. If you specify `true` when it has been disabled it will return an error.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasWiki

Set to `true` to enable the GitHub Wiki features on
the repository.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HomepageUrl

URL of a page describing the project.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseTemplate

Use the [name of the template](https://github.com/github/choosealicense.com/tree/gh-pages/_licenses) without the extension. For example, "mit" or "mpl-2.0".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the repository.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Private

Set to `true` to create a private repository.
Repositories are created as public (e.g. open source) by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Topics

The list of topics of the repository.

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

