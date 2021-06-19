# TF::AWS::LambdaCodeSigningConfig

Provides a Lambda Code Signing Config resource. A code signing configuration defines a list of allowed signing profiles and defines the code-signing validation policy (action to be taken if deployment validation checks fail).

For information about Lambda code signing configurations and how to use them, see [configuring code signing for Lambda functions][1]

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::LambdaCodeSigningConfig",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#allowedpublishers" title="AllowedPublishers">AllowedPublishers</a>" : <i>[ <a href="allowedpublishersdefinition.md">AllowedPublishersDefinition</a>, ... ]</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ <a href="policiesdefinition.md">PoliciesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::LambdaCodeSigningConfig
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#allowedpublishers" title="AllowedPublishers">AllowedPublishers</a>: <i>
      - <a href="allowedpublishersdefinition.md">AllowedPublishersDefinition</a></i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - <a href="policiesdefinition.md">PoliciesDefinition</a></i>
</pre>

## Properties

#### Description

Descriptive name for this code signing configuration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedPublishers

_Required_: No

_Type_: List of <a href="allowedpublishersdefinition.md">AllowedPublishersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

_Required_: No

_Type_: List of <a href="policiesdefinition.md">PoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### ConfigId

Returns the <code>ConfigId</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastModified

Returns the <code>LastModified</code> value.

