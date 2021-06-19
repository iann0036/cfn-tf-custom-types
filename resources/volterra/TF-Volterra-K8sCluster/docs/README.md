# TF::Volterra::K8sCluster

CloudFormation equivalent of volterra_k8s_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::K8sCluster",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#globalaccessenable" title="GlobalAccessEnable">GlobalAccessEnable</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#noclusterwideapps" title="NoClusterWideApps">NoClusterWideApps</a>" : <i>Boolean</i>,
        "<a href="#noglobalaccess" title="NoGlobalAccess">NoGlobalAccess</a>" : <i>Boolean</i>,
        "<a href="#noinsecureregistries" title="NoInsecureRegistries">NoInsecureRegistries</a>" : <i>Boolean</i>,
        "<a href="#nolocalaccess" title="NoLocalAccess">NoLocalAccess</a>" : <i>Boolean</i>,
        "<a href="#usedefaultclusterrolebindings" title="UseDefaultClusterRoleBindings">UseDefaultClusterRoleBindings</a>" : <i>Boolean</i>,
        "<a href="#usedefaultclusterroles" title="UseDefaultClusterRoles">UseDefaultClusterRoles</a>" : <i>Boolean</i>,
        "<a href="#usedefaultpsp" title="UseDefaultPsp">UseDefaultPsp</a>" : <i>Boolean</i>,
        "<a href="#clusterwideapplist" title="ClusterWideAppList">ClusterWideAppList</a>" : <i>[ <a href="clusterwideapplistdefinition.md">ClusterWideAppListDefinition</a>, ... ]</i>,
        "<a href="#insecureregistrylist" title="InsecureRegistryList">InsecureRegistryList</a>" : <i>[ <a href="insecureregistrylistdefinition.md">InsecureRegistryListDefinition</a>, ... ]</i>,
        "<a href="#localaccessconfig" title="LocalAccessConfig">LocalAccessConfig</a>" : <i>[ <a href="localaccessconfigdefinition.md">LocalAccessConfigDefinition</a>, ... ]</i>,
        "<a href="#usecustomclusterrolebindings" title="UseCustomClusterRoleBindings">UseCustomClusterRoleBindings</a>" : <i>[ <a href="usecustomclusterrolebindingsdefinition.md">UseCustomClusterRoleBindingsDefinition</a>, ... ]</i>,
        "<a href="#usecustomclusterrolelist" title="UseCustomClusterRoleList">UseCustomClusterRoleList</a>" : <i>[ <a href="usecustomclusterrolelistdefinition.md">UseCustomClusterRoleListDefinition</a>, ... ]</i>,
        "<a href="#usecustompsplist" title="UseCustomPspList">UseCustomPspList</a>" : <i>[ <a href="usecustompsplistdefinition.md">UseCustomPspListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::K8sCluster
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#globalaccessenable" title="GlobalAccessEnable">GlobalAccessEnable</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#noclusterwideapps" title="NoClusterWideApps">NoClusterWideApps</a>: <i>Boolean</i>
    <a href="#noglobalaccess" title="NoGlobalAccess">NoGlobalAccess</a>: <i>Boolean</i>
    <a href="#noinsecureregistries" title="NoInsecureRegistries">NoInsecureRegistries</a>: <i>Boolean</i>
    <a href="#nolocalaccess" title="NoLocalAccess">NoLocalAccess</a>: <i>Boolean</i>
    <a href="#usedefaultclusterrolebindings" title="UseDefaultClusterRoleBindings">UseDefaultClusterRoleBindings</a>: <i>Boolean</i>
    <a href="#usedefaultclusterroles" title="UseDefaultClusterRoles">UseDefaultClusterRoles</a>: <i>Boolean</i>
    <a href="#usedefaultpsp" title="UseDefaultPsp">UseDefaultPsp</a>: <i>Boolean</i>
    <a href="#clusterwideapplist" title="ClusterWideAppList">ClusterWideAppList</a>: <i>
      - <a href="clusterwideapplistdefinition.md">ClusterWideAppListDefinition</a></i>
    <a href="#insecureregistrylist" title="InsecureRegistryList">InsecureRegistryList</a>: <i>
      - <a href="insecureregistrylistdefinition.md">InsecureRegistryListDefinition</a></i>
    <a href="#localaccessconfig" title="LocalAccessConfig">LocalAccessConfig</a>: <i>
      - <a href="localaccessconfigdefinition.md">LocalAccessConfigDefinition</a></i>
    <a href="#usecustomclusterrolebindings" title="UseCustomClusterRoleBindings">UseCustomClusterRoleBindings</a>: <i>
      - <a href="usecustomclusterrolebindingsdefinition.md">UseCustomClusterRoleBindingsDefinition</a></i>
    <a href="#usecustomclusterrolelist" title="UseCustomClusterRoleList">UseCustomClusterRoleList</a>: <i>
      - <a href="usecustomclusterrolelistdefinition.md">UseCustomClusterRoleListDefinition</a></i>
    <a href="#usecustompsplist" title="UseCustomPspList">UseCustomPspList</a>: <i>
      - <a href="usecustompsplistdefinition.md">UseCustomPspListDefinition</a></i>
</pre>

## Properties

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalAccessEnable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoClusterWideApps

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoGlobalAccess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoInsecureRegistries

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoLocalAccess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDefaultClusterRoleBindings

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDefaultClusterRoles

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDefaultPsp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterWideAppList

_Required_: No

_Type_: List of <a href="clusterwideapplistdefinition.md">ClusterWideAppListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsecureRegistryList

_Required_: No

_Type_: List of <a href="insecureregistrylistdefinition.md">InsecureRegistryListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAccessConfig

_Required_: No

_Type_: List of <a href="localaccessconfigdefinition.md">LocalAccessConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCustomClusterRoleBindings

_Required_: No

_Type_: List of <a href="usecustomclusterrolebindingsdefinition.md">UseCustomClusterRoleBindingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCustomClusterRoleList

_Required_: No

_Type_: List of <a href="usecustomclusterrolelistdefinition.md">UseCustomClusterRoleListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCustomPspList

_Required_: No

_Type_: List of <a href="usecustompsplistdefinition.md">UseCustomPspListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

