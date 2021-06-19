# TF::AWS::LambdaCodeSigningConfig AllowedPublishersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#signingprofileversionarns" title="SigningProfileVersionArns">SigningProfileVersionArns</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#signingprofileversionarns" title="SigningProfileVersionArns">SigningProfileVersionArns</a>: <i>
      - String</i>
</pre>

## Properties

#### SigningProfileVersionArns

The Amazon Resource Name (ARN) for each of the signing profiles. A signing profile defines a trusted user who can sign a code package.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

