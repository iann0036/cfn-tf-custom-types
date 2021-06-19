# TF::Splunk::AuthorizationRoles

Create and update role information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Splunk::AuthorizationRoles",
    "Properties" : {
        "<a href="#capabilities" title="Capabilities">Capabilities</a>" : <i>[ String, ... ]</i>,
        "<a href="#cumulativerealtimesearchjobsquota" title="CumulativeRealtimeSearchJobsQuota">CumulativeRealtimeSearchJobsQuota</a>" : <i>Double</i>,
        "<a href="#cumulativesearchjobsquota" title="CumulativeSearchJobsQuota">CumulativeSearchJobsQuota</a>" : <i>Double</i>,
        "<a href="#defaultapp" title="DefaultApp">DefaultApp</a>" : <i>String</i>,
        "<a href="#importedroles" title="ImportedRoles">ImportedRoles</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#realtimesearchjobsquota" title="RealtimeSearchJobsQuota">RealtimeSearchJobsQuota</a>" : <i>Double</i>,
        "<a href="#searchdiskquota" title="SearchDiskQuota">SearchDiskQuota</a>" : <i>Double</i>,
        "<a href="#searchfilter" title="SearchFilter">SearchFilter</a>" : <i>String</i>,
        "<a href="#searchindexesallowed" title="SearchIndexesAllowed">SearchIndexesAllowed</a>" : <i>[ String, ... ]</i>,
        "<a href="#searchindexesdefault" title="SearchIndexesDefault">SearchIndexesDefault</a>" : <i>[ String, ... ]</i>,
        "<a href="#searchjobsquota" title="SearchJobsQuota">SearchJobsQuota</a>" : <i>Double</i>,
        "<a href="#searchtimewin" title="SearchTimeWin">SearchTimeWin</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Splunk::AuthorizationRoles
Properties:
    <a href="#capabilities" title="Capabilities">Capabilities</a>: <i>
      - String</i>
    <a href="#cumulativerealtimesearchjobsquota" title="CumulativeRealtimeSearchJobsQuota">CumulativeRealtimeSearchJobsQuota</a>: <i>Double</i>
    <a href="#cumulativesearchjobsquota" title="CumulativeSearchJobsQuota">CumulativeSearchJobsQuota</a>: <i>Double</i>
    <a href="#defaultapp" title="DefaultApp">DefaultApp</a>: <i>String</i>
    <a href="#importedroles" title="ImportedRoles">ImportedRoles</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#realtimesearchjobsquota" title="RealtimeSearchJobsQuota">RealtimeSearchJobsQuota</a>: <i>Double</i>
    <a href="#searchdiskquota" title="SearchDiskQuota">SearchDiskQuota</a>: <i>Double</i>
    <a href="#searchfilter" title="SearchFilter">SearchFilter</a>: <i>String</i>
    <a href="#searchindexesallowed" title="SearchIndexesAllowed">SearchIndexesAllowed</a>: <i>
      - String</i>
    <a href="#searchindexesdefault" title="SearchIndexesDefault">SearchIndexesDefault</a>: <i>
      - String</i>
    <a href="#searchjobsquota" title="SearchJobsQuota">SearchJobsQuota</a>: <i>Double</i>
    <a href="#searchtimewin" title="SearchTimeWin">SearchTimeWin</a>: <i>Double</i>
</pre>

## Properties

#### Capabilities

List of capabilities assigned to role.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CumulativeRealtimeSearchJobsQuota

Maximum number of concurrently running real-time searches that all members of this role can have.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CumulativeSearchJobsQuota

Maximum number of concurrently running searches for all role members. Warning message logged when limit is reached.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultApp

Specify the folder name of the default app to use for this role. A user-specific default app overrides this.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportedRoles

List of imported roles for this role. <br>Importing other roles imports all aspects of that role, such as capabilities and allowed indexes to search. In combining multiple roles, the effective value for each attribute is value with the broadest permissions.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the user role to create.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealtimeSearchJobsQuota

Specify the maximum number of concurrent real-time search jobs for this role. This count is independent from the normal search jobs limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchDiskQuota

Specifies the maximum disk space in MB that can be used by a user's search jobs. For example, a value of 100 limits this role to 100 MB total.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchFilter

Specify a search string that restricts the scope of searches run by this role. Search results for this role only show events that also match the search string you specify. In the case that a user has multiple roles with different search filters, they are combined with an OR.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchIndexesAllowed

List of indexes that this role has permissions to search. These may be wildcarded, but the index name must begin with an underscore to match internal indexes.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchIndexesDefault

List of indexes to search when no index is specified. These indexes can be wildcarded, with the exception that '*' does not match internal indexes. To match internal indexes, start with '_'. All internal indexes are represented by '_*'. A user with this role can search other indexes using "index= ".

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchJobsQuota

The maximum number of concurrent searches a user with this role is allowed to run. For users with multiple roles, the maximum quota value among all of the roles applies.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchTimeWin

Maximum time span of a search, in seconds. By default, searches are not limited to any specific time window. To override any search time windows from imported roles, set srchTimeWin to '0', as the 'admin' role does.

_Required_: No

_Type_: Double

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

