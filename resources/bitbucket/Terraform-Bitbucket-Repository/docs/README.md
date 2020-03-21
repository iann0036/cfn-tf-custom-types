# Terraform::Bitbucket::Repository

Provides a Bitbucket repository resource.

This resource allows you manage your repositories such as scm type, if it is
private, how to fork the repository and other options.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Bitbucket::Repository",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#forkpolicy" title="ForkPolicy">ForkPolicy</a>" : <i>String</i>,
        "<a href="#hasissues" title="HasIssues">HasIssues</a>" : <i>Boolean</i>,
        "<a href="#haswiki" title="HasWiki">HasWiki</a>" : <i>Boolean</i>,
        "<a href="#isprivate" title="IsPrivate">IsPrivate</a>" : <i>Boolean</i>,
        "<a href="#language" title="Language">Language</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
        "<a href="#pipelinesenabled" title="PipelinesEnabled">PipelinesEnabled</a>" : <i>Boolean</i>,
        "<a href="#projectkey" title="ProjectKey">ProjectKey</a>" : <i>String</i>,
        "<a href="#scm" title="Scm">Scm</a>" : <i>String</i>,
        "<a href="#slug" title="Slug">Slug</a>" : <i>String</i>,
        "<a href="#website" title="Website">Website</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Bitbucket::Repository
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#forkpolicy" title="ForkPolicy">ForkPolicy</a>: <i>String</i>
    <a href="#hasissues" title="HasIssues">HasIssues</a>: <i>Boolean</i>
    <a href="#haswiki" title="HasWiki">HasWiki</a>: <i>Boolean</i>
    <a href="#isprivate" title="IsPrivate">IsPrivate</a>: <i>Boolean</i>
    <a href="#language" title="Language">Language</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#owner" title="Owner">Owner</a>: <i>String</i>
    <a href="#pipelinesenabled" title="PipelinesEnabled">PipelinesEnabled</a>: <i>Boolean</i>
    <a href="#projectkey" title="ProjectKey">ProjectKey</a>: <i>String</i>
    <a href="#scm" title="Scm">Scm</a>: <i>String</i>
    <a href="#slug" title="Slug">Slug</a>: <i>String</i>
    <a href="#website" title="Website">Website</a>: <i>String</i>
</pre>

## Properties

#### Description

What the description of the repo is.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForkPolicy

What the fork policy should be. Defaults to
allow_forks.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasIssues

If this should have issues turned on or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasWiki

If this should have wiki turned on or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsPrivate

If this should be private or not. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Language

What the language of this repository should be.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the repository.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owner

The owner of this repository. Can be you or any team you
have write access to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PipelinesEnabled

Turn on to enable pipelines support.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectKey

If you want to have this repo associated with a
project.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scm

What SCM you want to use. Valid options are hg or git.
Defaults to git.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slug

The slug of the repository.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Website

URL of website associated with this repository.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CloneHttps

Returns the <code>CloneHttps</code> value.

#### CloneSsh

Returns the <code>CloneSsh</code> value.

