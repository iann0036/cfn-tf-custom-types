# TF::OCI::ApigatewayDeployment RequestPoliciesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authorization" title="Authorization">Authorization</a>" : <i>[ <a href="authorizationdefinition.md">AuthorizationDefinition</a>, ... ]</i>,
    "<a href="#bodyvalidation" title="BodyValidation">BodyValidation</a>" : <i>[ <a href="bodyvalidationdefinition.md">BodyValidationDefinition</a>, ... ]</i>,
    "<a href="#cors" title="Cors">Cors</a>" : <i>[ <a href="corsdefinition.md">CorsDefinition</a>, ... ]</i>,
    "<a href="#headertransformations" title="HeaderTransformations">HeaderTransformations</a>" : <i>[ <a href="headertransformationsdefinition.md">HeaderTransformationsDefinition</a>, ... ]</i>,
    "<a href="#headervalidations" title="HeaderValidations">HeaderValidations</a>" : <i>[ <a href="headervalidationsdefinition.md">HeaderValidationsDefinition</a>, ... ]</i>,
    "<a href="#queryparametertransformations" title="QueryParameterTransformations">QueryParameterTransformations</a>" : <i>[ <a href="queryparametertransformationsdefinition.md">QueryParameterTransformationsDefinition</a>, ... ]</i>,
    "<a href="#queryparametervalidations" title="QueryParameterValidations">QueryParameterValidations</a>" : <i>[ <a href="queryparametervalidationsdefinition.md">QueryParameterValidationsDefinition</a>, ... ]</i>,
    "<a href="#responsecachelookup" title="ResponseCacheLookup">ResponseCacheLookup</a>" : <i>[ <a href="responsecachelookupdefinition.md">ResponseCacheLookupDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authorization" title="Authorization">Authorization</a>: <i>
      - <a href="authorizationdefinition.md">AuthorizationDefinition</a></i>
<a href="#bodyvalidation" title="BodyValidation">BodyValidation</a>: <i>
      - <a href="bodyvalidationdefinition.md">BodyValidationDefinition</a></i>
<a href="#cors" title="Cors">Cors</a>: <i>
      - <a href="corsdefinition.md">CorsDefinition</a></i>
<a href="#headertransformations" title="HeaderTransformations">HeaderTransformations</a>: <i>
      - <a href="headertransformationsdefinition.md">HeaderTransformationsDefinition</a></i>
<a href="#headervalidations" title="HeaderValidations">HeaderValidations</a>: <i>
      - <a href="headervalidationsdefinition.md">HeaderValidationsDefinition</a></i>
<a href="#queryparametertransformations" title="QueryParameterTransformations">QueryParameterTransformations</a>: <i>
      - <a href="queryparametertransformationsdefinition.md">QueryParameterTransformationsDefinition</a></i>
<a href="#queryparametervalidations" title="QueryParameterValidations">QueryParameterValidations</a>: <i>
      - <a href="queryparametervalidationsdefinition.md">QueryParameterValidationsDefinition</a></i>
<a href="#responsecachelookup" title="ResponseCacheLookup">ResponseCacheLookup</a>: <i>
      - <a href="responsecachelookupdefinition.md">ResponseCacheLookupDefinition</a></i>
</pre>

## Properties

#### Authorization

_Required_: No

_Type_: List of <a href="authorizationdefinition.md">AuthorizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BodyValidation

_Required_: No

_Type_: List of <a href="bodyvalidationdefinition.md">BodyValidationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No

_Type_: List of <a href="corsdefinition.md">CorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderTransformations

_Required_: No

_Type_: List of <a href="headertransformationsdefinition.md">HeaderTransformationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderValidations

_Required_: No

_Type_: List of <a href="headervalidationsdefinition.md">HeaderValidationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryParameterTransformations

_Required_: No

_Type_: List of <a href="queryparametertransformationsdefinition.md">QueryParameterTransformationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryParameterValidations

_Required_: No

_Type_: List of <a href="queryparametervalidationsdefinition.md">QueryParameterValidationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCacheLookup

_Required_: No

_Type_: List of <a href="responsecachelookupdefinition.md">ResponseCacheLookupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

