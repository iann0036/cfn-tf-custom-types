# Terraform::OCI::ApigatewayDeployment Specification RequestPolicies

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authorization" title="Authorization">Authorization</a>" : <i>[ <a href="specification-requestpolicies-authorization.md">Authorization</a>, ... ]</i>,
    "<a href="#cors" title="Cors">Cors</a>" : <i>[ <a href="specification-requestpolicies-cors.md">Cors</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authorization" title="Authorization">Authorization</a>: <i>
      - <a href="specification-requestpolicies-authorization.md">Authorization</a></i>
<a href="#cors" title="Cors">Cors</a>: <i>
      - <a href="specification-requestpolicies-cors.md">Cors</a></i>
</pre>

## Properties

#### Authorization

_Required_: No
_Type_: List of <a href="specification-requestpolicies-authorization.md">Authorization</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No
_Type_: List of <a href="specification-requestpolicies-cors.md">Cors</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

