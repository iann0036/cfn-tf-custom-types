# TF::AVI::Cloud NsxtConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#automatedfwrules" title="AutomateDfwRules">AutomateDfwRules</a>" : <i>Boolean</i>,
    "<a href="#domainid" title="DomainId">DomainId</a>" : <i>String</i>,
    "<a href="#enforcementpointid" title="EnforcementpointId">EnforcementpointId</a>" : <i>String</i>,
    "<a href="#nsxtcredentialsref" title="NsxtCredentialsRef">NsxtCredentialsRef</a>" : <i>String</i>,
    "<a href="#nsxturl" title="NsxtUrl">NsxtUrl</a>" : <i>String</i>,
    "<a href="#siteid" title="SiteId">SiteId</a>" : <i>String</i>,
    "<a href="#datanetworkconfig" title="DataNetworkConfig">DataNetworkConfig</a>" : <i>[ <a href="datanetworkconfigdefinition.md">DataNetworkConfigDefinition</a>, ... ]</i>,
    "<a href="#managementnetworkconfig" title="ManagementNetworkConfig">ManagementNetworkConfig</a>" : <i>[ <a href="managementnetworkconfigdefinition.md">ManagementNetworkConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#automatedfwrules" title="AutomateDfwRules">AutomateDfwRules</a>: <i>Boolean</i>
<a href="#domainid" title="DomainId">DomainId</a>: <i>String</i>
<a href="#enforcementpointid" title="EnforcementpointId">EnforcementpointId</a>: <i>String</i>
<a href="#nsxtcredentialsref" title="NsxtCredentialsRef">NsxtCredentialsRef</a>: <i>String</i>
<a href="#nsxturl" title="NsxtUrl">NsxtUrl</a>: <i>String</i>
<a href="#siteid" title="SiteId">SiteId</a>: <i>String</i>
<a href="#datanetworkconfig" title="DataNetworkConfig">DataNetworkConfig</a>: <i>
      - <a href="datanetworkconfigdefinition.md">DataNetworkConfigDefinition</a></i>
<a href="#managementnetworkconfig" title="ManagementNetworkConfig">ManagementNetworkConfig</a>: <i>
      - <a href="managementnetworkconfigdefinition.md">ManagementNetworkConfigDefinition</a></i>
</pre>

## Properties

#### AutomateDfwRules

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforcementpointId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxtCredentialsRef

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxtUrl

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataNetworkConfig

_Required_: No

_Type_: List of <a href="datanetworkconfigdefinition.md">DataNetworkConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementNetworkConfig

_Required_: No

_Type_: List of <a href="managementnetworkconfigdefinition.md">ManagementNetworkConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

