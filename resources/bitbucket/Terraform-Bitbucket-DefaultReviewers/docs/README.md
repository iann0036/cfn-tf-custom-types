# Terraform::Bitbucket::DefaultReviewers

Provides support for setting up default reviewers for your repository. You must however have the UUID of the user available. Since Bitbucket has removed usernames from its APIs the best case is to use the UUID via the data provider.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Bitbucket::DefaultReviewers",
    "Properties" : {
        "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>,
        "<a href="#repository" title="Repository">Repository</a>" : <i>String</i>,
        "<a href="#reviewers" title="Reviewers">Reviewers</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Bitbucket::DefaultReviewers
Properties:
    <a href="#owner" title="Owner">Owner</a>: <i>String</i>
    <a href="#repository" title="Repository">Repository</a>: <i>String</i>
    <a href="#reviewers" title="Reviewers">Reviewers</a>: <i>
      - String</i>
</pre>

## Properties

#### Owner

The owner of this repository. Can be you or any team you
have write access to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repository

The name of the repository.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reviewers

A list of reviewers to use.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

