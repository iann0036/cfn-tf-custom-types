# TF::Volterra::K8sCluster ClusterWideAppsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#argocd" title="ArgoCd">ArgoCd</a>" : <i>[ <a href="argocddefinition.md">ArgoCdDefinition</a>, ... ]</i>,
    "<a href="#dashboard" title="Dashboard">Dashboard</a>" : <i>[ <a href="dashboarddefinition.md">DashboardDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#argocd" title="ArgoCd">ArgoCd</a>: <i>
      - <a href="argocddefinition.md">ArgoCdDefinition</a></i>
<a href="#dashboard" title="Dashboard">Dashboard</a>: <i>
      - <a href="dashboarddefinition.md">DashboardDefinition</a></i>
</pre>

## Properties

#### ArgoCd

_Required_: No

_Type_: List of <a href="argocddefinition.md">ArgoCdDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dashboard

_Required_: No

_Type_: List of <a href="dashboarddefinition.md">DashboardDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

