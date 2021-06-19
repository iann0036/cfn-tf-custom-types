# TF::FortiOS::SystemAccprofile LoggrpPermissionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#config" title="Config">Config</a>" : <i>String</i>,
    "<a href="#dataaccess" title="DataAccess">DataAccess</a>" : <i>String</i>,
    "<a href="#reportaccess" title="ReportAccess">ReportAccess</a>" : <i>String</i>,
    "<a href="#threatweight" title="ThreatWeight">ThreatWeight</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#config" title="Config">Config</a>: <i>String</i>
<a href="#dataaccess" title="DataAccess">DataAccess</a>: <i>String</i>
<a href="#reportaccess" title="ReportAccess">ReportAccess</a>: <i>String</i>
<a href="#threatweight" title="ThreatWeight">ThreatWeight</a>: <i>String</i>
</pre>

## Properties

#### Config

Log & Report configuration. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataAccess

Log & Report Data Access. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReportAccess

Log & Report Report Access. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatWeight

Log & Report Threat Weight. Valid values: `none`, `read`, `read-write`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

