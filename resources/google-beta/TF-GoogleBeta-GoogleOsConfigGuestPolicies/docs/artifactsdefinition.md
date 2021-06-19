# TF::GoogleBeta::GoogleOsConfigGuestPolicies ArtifactsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowinsecure" title="AllowInsecure">AllowInsecure</a>" : <i>Boolean</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#gcs" title="Gcs">Gcs</a>" : <i>[ <a href="gcsdefinition.md">GcsDefinition</a>, ... ]</i>,
    "<a href="#remote" title="Remote">Remote</a>" : <i>[ <a href="remotedefinition.md">RemoteDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowinsecure" title="AllowInsecure">AllowInsecure</a>: <i>Boolean</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#gcs" title="Gcs">Gcs</a>: <i>
      - <a href="gcsdefinition.md">GcsDefinition</a></i>
<a href="#remote" title="Remote">Remote</a>: <i>
      - <a href="remotedefinition.md">RemoteDefinition</a></i>
</pre>

## Properties

#### AllowInsecure

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gcs

_Required_: No

_Type_: List of <a href="gcsdefinition.md">GcsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Remote

_Required_: No

_Type_: List of <a href="remotedefinition.md">RemoteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

