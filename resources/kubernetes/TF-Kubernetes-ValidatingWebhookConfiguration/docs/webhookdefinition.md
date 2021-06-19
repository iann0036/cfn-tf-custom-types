# TF::Kubernetes::ValidatingWebhookConfiguration WebhookDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#admissionreviewversions" title="AdmissionReviewVersions">AdmissionReviewVersions</a>" : <i>[ String, ... ]</i>,
    "<a href="#failurepolicy" title="FailurePolicy">FailurePolicy</a>" : <i>String</i>,
    "<a href="#matchpolicy" title="MatchPolicy">MatchPolicy</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#sideeffects" title="SideEffects">SideEffects</a>" : <i>String</i>,
    "<a href="#timeoutseconds" title="TimeoutSeconds">TimeoutSeconds</a>" : <i>Double</i>,
    "<a href="#clientconfig" title="ClientConfig">ClientConfig</a>" : <i>[ <a href="clientconfigdefinition.md">ClientConfigDefinition</a>, ... ]</i>,
    "<a href="#namespaceselector" title="NamespaceSelector">NamespaceSelector</a>" : <i>[ <a href="namespaceselectordefinition.md">NamespaceSelectorDefinition</a>, ... ]</i>,
    "<a href="#objectselector" title="ObjectSelector">ObjectSelector</a>" : <i>[ <a href="objectselectordefinition.md">ObjectSelectorDefinition</a>, ... ]</i>,
    "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="ruledefinition.md">RuleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#admissionreviewversions" title="AdmissionReviewVersions">AdmissionReviewVersions</a>: <i>
      - String</i>
<a href="#failurepolicy" title="FailurePolicy">FailurePolicy</a>: <i>String</i>
<a href="#matchpolicy" title="MatchPolicy">MatchPolicy</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#sideeffects" title="SideEffects">SideEffects</a>: <i>String</i>
<a href="#timeoutseconds" title="TimeoutSeconds">TimeoutSeconds</a>: <i>Double</i>
<a href="#clientconfig" title="ClientConfig">ClientConfig</a>: <i>
      - <a href="clientconfigdefinition.md">ClientConfigDefinition</a></i>
<a href="#namespaceselector" title="NamespaceSelector">NamespaceSelector</a>: <i>
      - <a href="namespaceselectordefinition.md">NamespaceSelectorDefinition</a></i>
<a href="#objectselector" title="ObjectSelector">ObjectSelector</a>: <i>
      - <a href="objectselectordefinition.md">ObjectSelectorDefinition</a></i>
<a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="ruledefinition.md">RuleDefinition</a></i>
</pre>

## Properties

#### AdmissionReviewVersions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailurePolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SideEffects

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientConfig

_Required_: No

_Type_: List of <a href="clientconfigdefinition.md">ClientConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceSelector

_Required_: No

_Type_: List of <a href="namespaceselectordefinition.md">NamespaceSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectSelector

_Required_: No

_Type_: List of <a href="objectselectordefinition.md">ObjectSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="ruledefinition.md">RuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

