# TF::AWS::LambdaCodeSigningConfig PoliciesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#untrustedartifactondeployment" title="UntrustedArtifactOnDeployment">UntrustedArtifactOnDeployment</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#untrustedartifactondeployment" title="UntrustedArtifactOnDeployment">UntrustedArtifactOnDeployment</a>: <i>String</i>
</pre>

## Properties

#### UntrustedArtifactOnDeployment

Code signing configuration policy for deployment validation failure. If you set the policy to Enforce, Lambda blocks the deployment request if code-signing validation checks fail. If you set the policy to Warn, Lambda allows the deployment and creates a CloudWatch log. Valid values: `Warn`, `Enforce`. Default value: `Warn`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

